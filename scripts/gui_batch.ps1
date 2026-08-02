# Capture the control tree and a screenshot for every GUI tool, in one boot.
#
# Getting into the interactive session costs a reboot (see docs/GUI-FORMAT.md),
# so doing one tool per boot does not scale to a kit this size. This walks a
# list in a single session.
#
# Installers, uninstallers and updaters are excluded by the caller: they are
# PE subsystem 2 like any other GUI binary, but running an uninstaller to
# enumerate its buttons would be an expensive mistake.

$ErrorActionPreference = "Continue"
$out = "C:\gui-capture"
New-Item $out -ItemType Directory -Force | Out-Null
$summary = Join-Path $out "_summary.txt"
"# gui batch capture $(Get-Date -Format o)" | Out-File $summary -Encoding UTF8

Add-Type -AssemblyName UIAutomationClient, UIAutomationTypes, System.Drawing
. (Join-Path $PSScriptRoot "gui_capture.ps1")

$targets = Get-Content "C:\gui-targets.txt" | Where-Object { $_.Trim() }
$walker = [System.Windows.Automation.TreeWalker]::ControlViewWalker
$root = [System.Windows.Automation.AutomationElement]::RootElement

foreach ($line in $targets) {
    $parts = $line -split "\|", 2
    $name = $parts[0].Trim()
    $exe  = $parts[1].Trim()
    $log  = Join-Path $out "$name.tree.txt"

    "# gui-tree: $name"          | Out-File $log -Encoding UTF8
    "# exe: $exe"                | Out-File $log -Append -Encoding UTF8
    "# captured: $(Get-Date -Format o)" | Out-File $log -Append -Encoding UTF8

    $proc = $null
    try { $proc = Start-Process $exe -PassThru -ErrorAction Stop } catch {
        "# ERROR: $($_.Exception.Message)" | Out-File $log -Append -Encoding UTF8
        "$name`tSTART-FAILED`t0" | Out-File $summary -Append -Encoding UTF8
        continue
    }
    Start-Sleep -Seconds 10

    $win = $null
    foreach ($try in 1..4) {
        $child = $walker.GetFirstChild($root)
        while ($child) {
            try {
                if ($child.Current.ProcessId -eq $proc.Id -and $child.Current.Name) { $win = $child; break }
            } catch { }
            $child = $walker.GetNextSibling($child)
        }
        if ($win) { break }
        Start-Sleep -Seconds 3
    }

    if (-not $win) {
        "# ERROR: no top-level window" | Out-File $log -Append -Encoding UTF8
        "$name`tNO-WINDOW`t0" | Out-File $summary -Append -Encoding UTF8
        Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
        continue
    }

    "# window: $($win.Current.Name)"     | Out-File $log -Append -Encoding UTF8
    "# class: $($win.Current.ClassName)" | Out-File $log -Append -Encoding UTF8
    "#---"                               | Out-File $log -Append -Encoding UTF8

    $lines = New-Object System.Collections.Generic.List[string]
    $script:n = 0

    function Walk($el, $depth) {
        if ($script:n -ge 3000 -or $depth -gt 6) { return }
        $c2 = $walker.GetFirstChild($el)
        while ($c2) {
            if ($script:n -ge 3000) { return }
            $script:n++
            try {
                $cc = $c2.Current
                $type = $cc.ControlType.ProgrammaticName -replace "ControlType\.", ""
                $pad = "  " * $depth
                $bits = @("$pad$type")
                if ($cc.Name)         { $bits += "`"$($cc.Name)`"" }
                if ($cc.AutomationId) { $bits += "#$($cc.AutomationId)" }
                if ($cc.AccessKey)    { $bits += "[$($cc.AccessKey)]" }
                $lines.Add(($bits -join " "))
                if ($type -eq "MenuItem" -or $type -eq "Menu") {
                    $pat = $null
                    if ($c2.TryGetCurrentPattern(
                            [System.Windows.Automation.ExpandCollapsePattern]::Pattern, [ref]$pat)) {
                        try { $pat.Expand(); Start-Sleep -Milliseconds 200 } catch { }
                    }
                }
                Walk $c2 ($depth + 1)
            } catch { }
            $c2 = $walker.GetNextSibling($c2)
        }
    }

    Walk $win 0
    $lines | Out-File $log -Append -Encoding UTF8
    "#--- nodes: $($lines.Count)" | Out-File $log -Append -Encoding UTF8

    # PrintWindow, never CopyFromScreen. CopyFromScreen copies whatever pixels
    # are on the desktop inside a rectangle -- so a window smaller than its own
    # bounding box, or one that does not paint its background, publishes the
    # operator's taskbar, wallpaper and notifications. That happened twice.
    # PrintWindow asks the window to render itself into our bitmap; the desktop
    # is never read, and occlusion does not matter.
    Save-WindowImage -Win $win -Path (Join-Path $out "$name.png")

    "$name`tOK`t$($lines.Count)" | Out-File $summary -Append -Encoding UTF8

    Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
    Start-Sleep -Seconds 2
}

"# done" | Out-File $summary -Append -Encoding UTF8
New-Item C:\gui-batch-done.txt -ItemType File -Force | Out-Null
