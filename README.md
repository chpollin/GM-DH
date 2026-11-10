# Angewandte Generative KI in den (digitalen) Geisteswissenschaften

Static website of the workshop and talk series on applied generative AI in the (digital) humanities, published at https://chpollin.github.io/GM-DH. It lists talks, workshops, slides and videos with preview images.

## Contents

- `index.html`, `css/`, `js/` and `img/` form the site, served by GitHub Pages from the repository root.
- `workshop-pages/` holds the pages of individual workshops and `slides/` the slide decks as PDF.
- `prompts/` holds the PRISM prompt in `PRISM.md`, from which `generate_prompts_html.py` writes `prompts.html` into the current directory.
- `scripts/gpt-api-python/` holds code examples for the GPT API used in the workshops.

## Running locally

The site needs no build step. Serve the repository root and open the page:

```
python -m http.server 8000
```

Then open http://127.0.0.1:8000/.

## Citation and licence

Citation metadata are in `CITATION.cff`, which declares CC BY 4.0.
