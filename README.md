# Global Alignment CLI + Web UI

This project provides:

- A CLI `cli_align.py` that computes the global alignment score (Needleman–Wunsch).
- A minimal Flask web app (`app.py`) with a modern black-and-white UI to compute alignments in the browser.

Quick start

1. Create a virtualenv and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run CLI:

```bash
python cli_align.py ACTG ACGT --show-alignment
```

3. Run web app:

```bash
python app.py
# open http://127.0.0.1:5000
```

Files

- `cli_align.py` — CLI and core global alignment implementation
- `app.py` — Flask server and `/api/align` JSON endpoint
- `templates/index.html` — black & white website
- `static/css/style.css` — styles
- `static/js/app.js` — client JS
