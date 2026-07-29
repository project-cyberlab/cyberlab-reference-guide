<!-- generated-by: scripts/generate_pages.py -->
# cyberchef

**Kit:** REMnux · FLARE-VM · Security Onion  **Capability:** Decode, decrypt or transform encoded data
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/cyberchef.help.txt)  **Docs:** <https://github.com/gchq/CyberChef/>

## Purpose

Decode and otherwise analyze data using this browser app.

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 09-deobfuscation
cyberchef &
# from cyberlab 25-cyberchef-recipes
cyberchef --help | head -n 5
# from cyberlab 25-cyberchef-recipes
cyberchef --recipe "From Base64" --input encoded_payload.ps1.txt 2>/dev/null | cyberchef --recipe "XOR({'option':'Hex','value':'2a'})" | cyberchef --recipe "Gunzip"
# from cyberlab 25-cyberchef-recipes
cyberchef --recipe "From Base64" --input encoded_payload.ps1.txt | cyberchef --recipe "XOR({'option':'Hex','value':'2a'})" | cyberchef --recipe "Gunzip" | tee /tmp/decoded.txt | sha256sum
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

`base64dump.py`, `rax2`, `xxd`, `openssl`, `numbers-to-string.py`
