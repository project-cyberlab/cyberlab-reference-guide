# The build has an ordering dependency that is easy to trip over by hand:
#
#     enrichment.py  ->  generate_pages.py  ->  build_pdf.py
#
# Editing curation and jumping straight to the PDF publishes pages that do not
# contain the edit, silently and with no error. That happened once already, so
# the sequence lives here rather than in anyone's memory.

PY ?= python

.PHONY: all pages pdf lint check clean

all: check

# Regenerate every tool page from the captures plus the judgement layer.
pages:
	$(PY) scripts/generate_pages.py
	$(PY) scripts/build_index.py

# Always regenerate first: a PDF built from stale pages is the failure this
# file exists to prevent.
pdf: pages
	$(PY) scripts/build_pdf.py

# The gate. Errors fail the build; warnings are tracked debt.
lint: pages
	$(PY) scripts/lint.py

# What to run before committing.
check: pages lint pdf
	@echo "--- published artifact ---"
	@$(PY) -c "from pypdf import PdfReader; import os; \
r=PdfReader('CyberLab-Reference-Guide.pdf'); \
w=lambda i:[x for x in i]; \
print('  CyberLab-Reference-Guide.pdf', format(os.path.getsize('CyberLab-Reference-Guide.pdf'),','), 'bytes,', len(r.pages), 'pages')"

# Coverage is rebuilt from the container probes, not from anything here; see
# capture/cyberlab-aio-v2.Dockerfile and v3 for how the images are produced.
coverage:
	$(PY) scripts/merge_coverage.py

clean:
	rm -rf build/
