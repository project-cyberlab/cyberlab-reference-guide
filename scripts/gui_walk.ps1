# Walk a GUI application's automation tree and capture it as evidence.
#
# This is the GUI equivalent of running --help and keeping the output: a
# machine-readable enumeration of every menu, pane, button and field, written
# to capture/ so a page can be linted against it.
#
# Must run in the interactive desktop session (session 1). Session 0 has no
# window station, so the tree comes back empty.
#
# The earlier version used FindAll(Descendants) on the top-level window, which
# returns almost nothing for applications whose content is virtualised (modern
# XAML, Qt, Java). A TreeWalker recursion reaches those, and menus are expanded
# where the pattern is available, because an unexpanded menu bar reports only
# its top-level items -- exactly the part a reader already knows.

param(
    [string]$Exe,
    [string]$Name,
    [int]$Wait = 12,
    [int]$MaxDepth = 6,
    [int]$MaxNodes = 4000
)

$ErrorActionPreference = "Continue"
$out = "C:\gui-capture"
New-Item $out -ItemType Directory -Force | Out-Null
$log = Join-Path $out "$Name.tree.txt"

Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, System.Drawing

"# gui-tree: $Name"                                    | Out-File $log -Encoding UTF8
"# exe: $Exe"                                          | Out-File $log -Append -Encoding UTF8
"# captured: $(Get-Date -Format o)"                     | Out-File $log -Append -Encoding UTF8
"# session: $((Get-Process -Id $PID).SessionId)"        | Out-File $log -Append -Encoding UTF8

$proc = Start-Process $Exe -PassThru -ErrorAction SilentlyContinue
if (-not $proc) { "# ERROR: could not start" | Out-File $log -Append -Encoding UTF8; exit 1 }
Start-Sleep -Seconds $Wait

# The process that starts is not always the one that owns the window
# (launchers, splash screens), so find any top-level window of that name.
$root = [System.Windows.Automation.AutomationElement]::RootElement
$walker = [System.Windows.Automation.TreeWalker]::ControlViewWalker

$win = $null
foreach ($try in 1..6) {
    $child = $walker.GetFirstChild($root)
    while ($child) {
        try {
            $pid2 = $child.Current.ProcessId
            $p = Get-Process -Id $pid2 -ErrorAction SilentlyContinue
            if ($p -and ($p.Id -eq $proc.Id -or $p.ProcessName -like "*$Name*")) {
                if ($child.Current.Name) { $win = $child; break }
            }
        } catch { }
        $child = $walker.GetNextSibling($child)
    }
    if ($win) { break }
    Start-Sleep -Seconds 3
}

if (-not $win) {
    "# ERROR: no top-level window found" | Out-File $log -Append -Encoding UTF8
    Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
    exit 1
}

"# window: $($win.Current.Name)"        | Out-File $log -Append -Encoding UTF8
"# class: $($win.Current.ClassName)"    | Out-File $log -Append -Encoding UTF8
"#---"                                  | Out-File $log -Append -Encoding UTF8

$script:count = 0
$lines = New-Object System.Collections.Generic.List[string]

function Walk($el, $depth) {
    if ($script:count -ge $MaxNodes -or $depth -gt $MaxDepth) { return }
    $child = $walker.GetFirstChild($el)
    while ($child) {
        if ($script:count -ge $MaxNodes) { return }
        $script:count++
        try {
            $c = $child.Current
            $type = $c.ControlType.ProgrammaticName -replace "ControlType\.", ""
            $name = $c.Name
            $id   = $c.AutomationId
            $key  = $c.AccessKey
            $pad  = "  " * $depth
            $bits = @("$pad$type")
            if ($name) { $bits += "`"$name`"" }
            if ($id)   { $bits += "#$id" }
            if ($key)  { $bits += "[$key]" }
            $lines.Add(($bits -join " "))

            # A collapsed menu reports only its own label, so expand it: the
            # submenu items are the part worth documenting.
            if ($type -eq "MenuItem" -or $type -eq "Menu") {
                $pattern = $null
                if ($child.TryGetCurrentPattern(
                        [System.Windows.Automation.ExpandCollapsePattern]::Pattern, [ref]$pattern)) {
                    try { $pattern.Expand(); Start-Sleep -Milliseconds 250 } catch { }
                }
            }
            Walk $child ($depth + 1)
        } catch { }
        $child = $walker.GetNextSibling($child)
    }
}

Walk $win 0
$lines | Out-File $log -Append -Encoding UTF8
"#--- nodes: $($lines.Count)" | Out-File $log -Append -Encoding UTF8

# Screenshot of the window as it was enumerated.
try {
    $r = $win.Current.BoundingRectangle
    if ($r.Width -gt 0 -and $r.Height -gt 0) {
        $bmp = New-Object System.Drawing.Bitmap([int]$r.Width, [int]$r.Height)
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.CopyFromScreen([int]$r.X, [int]$r.Y, 0, 0, $bmp.Size)
        $bmp.Save((Join-Path $out "$Name.png"), [System.Drawing.Imaging.ImageFormat]::Png)
        $g.Dispose(); $bmp.Dispose()
    }
} catch { "# screenshot failed: $($_.Exception.Message)" | Out-File $log -Append -Encoding UTF8 }

Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
Get-Process -Name $Name -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
