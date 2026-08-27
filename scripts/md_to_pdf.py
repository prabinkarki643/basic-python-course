"""Convert a Markdown file to a print-ready A4 PDF.

Pipeline: Markdown -> HTML (mistune) -> PDF (headless Chrome).
No network access and no extra installs are required.

Usage:
    python3 scripts/md_to_pdf.py SUMMARY.md SUMMARY.pdf
"""

import pathlib
import re
import subprocess
import sys

import mistune

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page {
    size: A4;
    margin: 18mm 16mm 20mm 16mm;
}

* { box-sizing: border-box; }

body {
    font-family: "Georgia", "Times New Roman", serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1a1a1a;
    margin: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* ---------- Headings ---------- */

h1 {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 21pt;
    line-height: 1.2;
    color: #0f2942;
    margin: 0 0 4pt 0;
    padding-bottom: 8pt;
    border-bottom: 2.5pt solid #0f2942;
}

h2 {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 14pt;
    color: #0f2942;
    margin: 22pt 0 8pt 0;
    padding-bottom: 4pt;
    border-bottom: 0.75pt solid #c8d2dc;
    page-break-after: avoid;
    break-after: avoid;
}

h3 {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 11pt;
    color: #1c3d5a;
    margin: 14pt 0 5pt 0;
    page-break-after: avoid;
    break-after: avoid;
}

h2 + h3 { margin-top: 10pt; }

/* ---------- Text ---------- */

p { margin: 0 0 8pt 0; }

strong { color: #0f2942; }

a {
    color: #1c3d5a;
    text-decoration: none;
    border-bottom: 0.5pt solid #9fb3c4;
}

hr {
    border: none;
    border-top: 0.75pt solid #d8dfe6;
    margin: 18pt 0;
}

/* ---------- Lists ---------- */

ul, ol { margin: 0 0 9pt 0; padding-left: 18pt; }
li { margin-bottom: 3pt; }
li > ul, li > ol { margin-top: 3pt; margin-bottom: 0; }

/* Checklist bullets from "- [ ]" */
li input[type="checkbox"] {
    margin-right: 5pt;
    transform: scale(0.9);
}
ul:has(> li > input[type="checkbox"]) { list-style: none; padding-left: 4pt; }

/* ---------- Tables ---------- */

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10pt 0 14pt 0;
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 9pt;
    page-break-inside: avoid;
    break-inside: avoid;
}

thead { background: #0f2942; }

th {
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 6pt 7pt;
    border: 0.5pt solid #0f2942;
}

td {
    padding: 5pt 7pt;
    border: 0.5pt solid #ccd5de;
    vertical-align: top;
}

tbody tr:nth-child(even) { background: #f4f7fa; }

/* Headerless "label / value" tables: style the first column as row labels */
table:not(:has(thead)) td:first-child {
    width: 30%;
    font-weight: 600;
    color: #0f2942;
}

/* Right-aligned numeric columns keep their alignment */
th[align="right"], td[align="right"] { text-align: right; }
th[align="center"], td[align="center"] { text-align: center; }

/* ---------- Code ---------- */

code {
    font-family: "SF Mono", "Menlo", "Consolas", monospace;
    font-size: 8.8pt;
    background: #eef2f6;
    padding: 1pt 3.5pt;
    border-radius: 2pt;
    color: #0b3d2c;
}

pre {
    background: #f6f8fa;
    border: 0.5pt solid #d8dfe6;
    border-left: 2.5pt solid #0f2942;
    padding: 8pt 10pt;
    overflow-x: auto;
    page-break-inside: avoid;
    break-inside: avoid;
}

pre code {
    background: none;
    padding: 0;
    font-size: 8.5pt;
    line-height: 1.45;
    color: #1a1a1a;
}

/* ---------- Blockquote callouts ---------- */

blockquote {
    margin: 10pt 0;
    padding: 7pt 11pt;
    background: #fbf7ec;
    border-left: 2.5pt solid #b8892b;
    page-break-inside: avoid;
    break-inside: avoid;
}

blockquote p { margin: 0; }

/* ---------- Page-break control ---------- */

h2 { page-break-before: auto; }

/* Keep the budget section intact on one page where possible */
h2#budget { page-break-before: always; break-before: page; }
"""

HTML_SHELL = """<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{content}
</body>
</html>
"""


def slugify(text):
    """Turn heading text into an id usable by the CSS page-break rules."""
    keep = []
    for ch in text.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_":
            keep.append("-")
    return "".join(keep).strip("-")


class HeadingIdRenderer(mistune.HTMLRenderer):
    """Adds an id to every heading so stylesheets can target sections."""

    def heading(self, text, level, **attrs):
        plain = mistune.util.striptags(text)
        return f'<h{level} id="{slugify(plain)}">{text}</h{level}>\n'


EMPTY_THEAD = re.compile(
    r"<thead>\s*<tr>(?:\s*<th[^>]*>\s*</th>)+\s*</tr>\s*</thead>", re.S
)


def drop_empty_headers(html):
    """Remove table header rows whose cells are all empty.

    Markdown requires a header row, so a two-column "label / value" table is
    written with an empty one. Left in place it renders as a solid dark bar.
    """
    return EMPTY_THEAD.sub("", html)


def convert(md_path, pdf_path):
    md_file = pathlib.Path(md_path)
    pdf_file = pathlib.Path(pdf_path)

    markdown = mistune.create_markdown(
        renderer=HeadingIdRenderer(escape=False),
        plugins=["table", "strikethrough", "task_lists", "url"],
        hard_wrap=True,
    )

    content = drop_empty_headers(markdown(md_file.read_text(encoding="utf-8")))
    title = md_file.stem.replace("-", " ").replace("_", " ")

    html_file = pdf_file.with_suffix(".html")
    html_file.write_text(
        HTML_SHELL.format(title=title, css=CSS, content=content),
        encoding="utf-8",
    )

    subprocess.run(
        [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=10000",
            f"--print-to-pdf={pdf_file.resolve()}",
            html_file.resolve().as_uri(),
        ],
        check=True,
        capture_output=True,
    )

    html_file.unlink()

    size_kb = pdf_file.stat().st_size / 1024
    print(f"Written {pdf_file} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
