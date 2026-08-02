# cyberlab-aio:v2 — adds the acquisition tooling the kit was missing.
#
# Why this exists
# ---------------
# The guide's "Acquire & preserve" capability lists the E01 and AFF suites, but
# nothing in the kit actually carried them: the SIFT VM turned out to be a bare
# Ubuntu 20.04 install with none of its toolset, and cyberlab-aio:v1 had no
# ewf-tools or afflib-tools either. Under capture-or-it-does-not-ship those
# pages could not be written at all — the most fundamental step in the workflow
# was the least documented part of the guide.
#
# Measured before this change: of 38 representative SIFT commands, 22 were
# captured and 16 were unavailable anywhere in the kit.
#
# Build on the Docker host that holds cyberlab-aio:v1:
#     docker build -t cyberlab-aio:v2 -f cyberlab-aio-v2.Dockerfile .
#
# Then re-probe and re-merge:
#     docker run --rm -v $PWD/scripts/probe_container.sh:/probe.sh:ro \
#                     -v $PWD/capture/_candidates.txt:/cands.txt:ro \
#                     -v /tmp/probeout:/out cyberlab-aio:v2 bash /probe.sh /cands.txt /out
#     python scripts/merge_coverage.py && python scripts/generate_pages.py
#
# v1 is left untouched: the existing 945 captures were taken against it, and
# retagging in place would invalidate the provenance recorded in every page
# header.

FROM cyberlab-aio:v1

# bulk-extractor is deliberately absent: it was dropped from Debian and is in
# neither bookworm nor bookworm-backports. It needs a source build or a
# third-party package, so it is tracked as an open gap rather than silently
# omitted.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        afflib-tools \
        aircrack-ng \
        arp-scan \
        cabextract \
        ccrypt \
        cryptsetup-bin \
        dc3dd \
        dcfldd \
        disktype \
        dislocker \
        ewf-tools \
        libimage-exiftool-perl \
    && rm -rf /var/lib/apt/lists/*
