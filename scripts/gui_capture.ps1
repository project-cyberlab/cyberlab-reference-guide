# Window capture that cannot photograph the operator's desktop.
#
# The obvious way to screenshot a window is to take its bounding rectangle and
# copy that region of the screen. It is also wrong, and it published this
# operator's taskbar, pinned icons, weather widget and clock into a shipped PDF
# -- twice. A screen copy reads *the desktop*, so anything the window does not
# itself paint over comes along: the gap between a window's reported bounds and
# its drawn area, any overlapping window, the shell.
#
# PrintWindow instead sends WM_PRINT to the window and the window renders
# itself into a device context we own. Nothing outside the window is ever read,
# and the result is correct even if the window is occluded or off-screen.
#
# PW_RENDERFULLCONTENT (2) is required for anything drawing through DirectX or
# a modern composition path; without it those windows return a blank bitmap.

if (-not ('Native.Win' -as [type])) {
    Add-Type -Namespace Native -Name Win -MemberDefinition @'
[DllImport("user32.dll")]
public static extern bool PrintWindow(IntPtr hwnd, IntPtr hdc, uint flags);
[DllImport("user32.dll")]
public static extern bool GetWindowRect(IntPtr hwnd, out RECT rect);
[StructLayout(LayoutKind.Sequential)]
public struct RECT { public int Left, Top, Right, Bottom; }
'@
}

function Save-WindowImage {
    param(
        [Parameter(Mandatory)] $Win,     # AutomationElement
        [Parameter(Mandatory)] [string] $Path
    )
    try {
        $hwnd = [IntPtr]$Win.Current.NativeWindowHandle
        if ($hwnd -eq [IntPtr]::Zero) { return $false }

        $rect = New-Object Native.Win+RECT
        if (-not [Native.Win]::GetWindowRect($hwnd, [ref]$rect)) { return $false }
        $w = $rect.Right - $rect.Left
        $h = $rect.Bottom - $rect.Top
        if ($w -le 0 -or $h -le 0 -or $w -gt 10000 -or $h -gt 10000) { return $false }

        $bmp = New-Object System.Drawing.Bitmap($w, $h)
        $g   = [System.Drawing.Graphics]::FromImage($bmp)
        $hdc = $g.GetHdc()
        # 2 = PW_RENDERFULLCONTENT. Fall back to 0 for old windows that
        # refuse the flag and return false.
        $ok = [Native.Win]::PrintWindow($hwnd, $hdc, 2)
        if (-not $ok) { $ok = [Native.Win]::PrintWindow($hwnd, $hdc, 0) }
        $g.ReleaseHdc($hdc)
        $g.Dispose()

        if ($ok) {
            # A window that rendered nothing is not worth shipping: an empty
            # frame teaches less than no image at all, which is the other half
            # of the review feedback on these screenshots.
            if (Test-BitmapBlank $bmp) {
                $bmp.Dispose()
                Write-Host "  $Path : window rendered blank, not saved"
                return $false
            }
            $bmp.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
        }
        $bmp.Dispose()
        return $ok
    } catch {
        Write-Host "  capture failed: $_"
        return $false
    }
}

function Test-BitmapBlank {
    param([Parameter(Mandatory)] $bmp)
    # Sample a grid rather than every pixel; we only need to know whether the
    # window drew anything beyond a single flat fill.
    $seen = @{}
    for ($x = 4; $x -lt $bmp.Width; $x += [Math]::Max(1, [int]($bmp.Width / 40))) {
        for ($y = 4; $y -lt $bmp.Height; $y += [Math]::Max(1, [int]($bmp.Height / 40))) {
            $seen[$bmp.GetPixel($x, $y).ToArgb()] = $true
            if ($seen.Count -gt 6) { return $false }
        }
    }
    return $true
}
