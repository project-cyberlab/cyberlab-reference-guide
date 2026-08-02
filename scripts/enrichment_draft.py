"""Model-drafted guidance awaiting review.

NOT loaded by the build. Every line here was written by a local
model from a tool's captured help and survived validation, which
means it is grounded and specific -- not that it is correct.
Read it, fix it, move it into enrichment.py.
"""

DRAFT = {
    "pdf-parser": {
        "-s": "When you need to find specific strings in indirect objects but not within streams.",
        "-f": "When you want to see the decoded content of filtered streams.",
        "-o": "When you are interested in examining specific indirect objects by their IDs.",
        "-r": "When you want to trace references between indirect objects.",
        "-a": "When you are analyzing the structure of a PDF document and need statistical information.",
        "-O": "When you suspect malicious content within /ObjStm (object stream) objects.",
        "-H": "When you want to verify the integrity of objects using hash values.",
        "-n": "When you prefer non-canonicalized output for specific analysis needs.",
        "-D": "When debugging or troubleshooting issues with PDF parsing.",
        "--searchstream": "When searching for specific strings within filtered streams.",
        "--unfiltered": "When you need to search within unfiltered stream data.",
        "--regex": "When using regular expressions to search within streams.",
        "--overridingfilters": "When you want to override the default filters with custom ones.",
        "--generateembedded": "When embedding selected indirect objects as files in a generated Python script.",
        "-y": "When applying YARA rules to check streams for malicious content.",
        "--yarastrings": "When you need to see the strings used by YARA rules.",
        "--decoders": "When loading specific decoders to handle particular stream types.",
        "--decoderoptions": "When configuring options for custom decoders.",
        "-k": "When searching for specific keys within dictionaries in the PDF."
    }
}
