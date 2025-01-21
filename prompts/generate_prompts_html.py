#!/usr/bin/env python3

"""
generate_prompts_html.py

Iterates over all Markdown files in the current directory (or a specified path),
parses out the sections "# Description" and "# PRISM: Parameterized Recursive Insight Synthesis Matrix",
then generates a single HTML file using the provided index.html snippet as a template.

In the output HTML:
  - Prompts are displayed in a 3-column Bootstrap 5 grid (cards).
  - Only the "# PRISM" section (treated as the 'system prompt') has a "Copy me" button.
    Clicking the button copies the PRISM content to the clipboard.

Requires:
 - python-markdown (install via pip: pip install markdown)

Usage:
  1. Place this script in the same directory as your .md files (or adjust the path in 'markdown_dir').
  2. Run: python generate_prompts_html.py
  3. An output file named "prompts.html" will be created in the current directory.
"""

import os
import re
import markdown

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------
markdown_dir = "."  # Directory containing the .md files
output_html_file = "prompts.html"
css_path = "../css/style.css"

# Regex patterns to extract sections
description_pattern = re.compile(
    r"(?s)# Description\s+(.*?)(?=# PRISM|$)", re.IGNORECASE
)
prism_pattern = re.compile(
    r"(?s)# PRISM: Parameterized Recursive Insight Synthesis Matrix\s+(.*)", re.IGNORECASE
)

# ---------------------------------------------------------------------
# Template: We embed the provided HTML snippet.
# We'll insert generated content into <!-- INSERT CONTENT HERE -->
# ---------------------------------------------------------------------
template_html = f"""<!doctype html>
<html lang="de">

<head>
    <!-- Erforderliche Metatags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Workshop series on Applied Generative AI in Digital Humanities by Christopher Pollin">
    <meta name="author" content="Christopher Pollin">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
          crossorigin="anonymous"/>
    <!-- Custom CSS -->
    <link href="{css_path}" rel="stylesheet"/>
    <title>Angewandte Generative KI in den (digitalen) Geisteswissenschaften</title>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light" aria-label="Hauptnavigation">
            <div class="container">
                <a class="navbar-brand" href="../index.html">AGKI Prompts</a>
                <button class="navbar-toggler" type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Navigation umschalten">
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
        </nav>
    </header>

    <main>
        <div class="container mt-4">
            <!-- INSERT CONTENT HERE -->
        </div>
    </main>

    <footer class="footer mt-auto py-3 bg-light">
        <div class="container">
            <span class="text-muted">© 2025 <a href="https://chpollin.github.io/" target="_blank" rel="noopener noreferrer">Christopher Pollin</a>, 8020 Graz - Austria.</span>
        </div>
    </footer>

    <!-- Bootstrap Bundle mit Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
            crossorigin="anonymous"></script>

    <script>
    // Copies the PRISM (system prompt) content to clipboard
    function copySystemPrompt(id) {{
        let textToCopy = document.getElementById("systemPrompt-" + id).innerText;
        navigator.clipboard.writeText(textToCopy)
            .then(() => {{
                alert("System prompt copied to clipboard!");
            }})
            .catch(err => {{
                console.error('Failed to copy: ', err);
            }});
    }}
    </script>
</body>
</html>
"""

# ---------------------------------------------------------------------
# Function to parse each Markdown file, returning HTML segments
# ---------------------------------------------------------------------
def parse_markdown_file(filepath):
    """
    Returns a tuple (description_html, prism_html) extracted from the Markdown file.
    If a section is not found, returns an empty string for that section.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the "# Description" section
    desc_match = description_pattern.search(content)
    description_content = desc_match.group(1).strip() if desc_match else ""

    # Extract the "# PRISM" section
    prism_match = prism_pattern.search(content)
    prism_content = prism_match.group(1).strip() if prism_match else ""

    # Convert to HTML using python-markdown
    description_html = markdown.markdown(description_content) if description_content else ""
    prism_html = markdown.markdown(prism_content) if prism_content else ""

    return (description_html, prism_html)

# ---------------------------------------------------------------------
# Main script
# ---------------------------------------------------------------------
def main():
    entries = []

    # Iterate over .md files
    for filename in os.listdir(markdown_dir):
        if filename.lower().endswith(".md"):
            filepath = os.path.join(markdown_dir, filename)
            desc_html, prism_html = parse_markdown_file(filepath)

            # Only add if there's at least one non-empty section
            if desc_html or prism_html:
                entries.append((filename, desc_html, prism_html))

    # Build the HTML content to be inserted:
    #  3-column grid of cards, each card = one MD file's content
    content_html = []
    content_html.append('<div class="row row-cols-1 row-cols-md-3 g-4">')

    for (filename, desc_html, prism_html) in entries:
        card_snippet = f"""
        <div class="col">
          <div class="card h-100">
            <div class="card-header bg-secondary text-white">
                {filename}
            </div>
            <div class="card-body">
        """

        if desc_html:
            card_snippet += f"""
                <h2># Description</h2>
                {desc_html}
            """

        if prism_html:
            # Here we treat the PRISM section as the 'system prompt' and add a "Copy me" button
            card_snippet += f"""
                <hr/>
                <h2># PRISM: Parameterized Recursive Insight Synthesis Matrix</h2>
                <div class="system-prompt" id="systemPrompt-{filename}">
                    {prism_html}
                </div>
                <button class="btn btn-primary mt-2" onclick="copySystemPrompt('{filename}')">Copy me</button>
            """

        card_snippet += """
            </div>
          </div>
        </div>
        """
        content_html.append(card_snippet)

    content_html.append('</div>')  # close .row

    final_content_html = "\n".join(content_html)
    # Insert into the template
    final_html = template_html.replace("<!-- INSERT CONTENT HERE -->", final_content_html)

    # Write to file
    with open(output_html_file, "w", encoding="utf-8") as out:
        out.write(final_html)

    print(f"Done. Generated {output_html_file} with {len(entries)} prompt entries.")

if __name__ == "__main__":
    main()
