# cyberlab-aio:v3 — v2 plus bulk_extractor, built from source.
#
# Why a source build
# ------------------
# bulk_extractor is listed as a Phase-5 priority tool and appears under three
# capabilities in the index, but it is packaged nowhere we can reach: it was
# dropped from Debian (absent from bookworm and bookworm-backports) and is no
# longer in kali-rolling either. Verified by pulling both package indices, not
# by assumption. A source build is the only way to document it from a real
# binary, which the capture-or-it-does-not-ship rule requires.
#
# The build is multi-stage on purpose. Compiling needs build-essential,
# autoconf, flex, bison and the -dev headers, roughly 400 MB of toolchain that
# has no business in a forensic analysis image. Only the finished binary and
# its runtime libraries are carried into the final layer.
#
# configure fails without RE2 (libre2-dev). That is not in the upstream
# dependency list in the wiki, which still describes 1.x, so it is recorded
# here.
#
# Build (on the host holding cyberlab-aio:v2):
#     docker build -t cyberlab-aio:v3 -f cyberlab-aio-v3.Dockerfile .

FROM cyberlab-aio:v2 AS builder

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential autoconf automake libtool flex bison git ca-certificates \
        libewf-dev libssl-dev zlib1g-dev libexpat1-dev pkg-config libre2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 --recurse-submodules --shallow-submodules \
        https://github.com/simsong/bulk_extractor.git /src/bulk_extractor \
    && cd /src/bulk_extractor \
    && ./bootstrap.sh \
    && ./configure --quiet \
    && make -j"$(nproc)" \
    && make install


FROM cyberlab-aio:v2

# Runtime libraries only: the -dev headers and the compiler stay behind.
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        libre2-9 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/bin/bulk_extractor /usr/local/bin/bulk_extractor

RUN bulk_extractor -V
