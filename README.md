# AI FIR Draft Assistant

A Flask web app that helps draft **First Information Report (FIR)** text from structured inputs, with a modern UI and export to **PDF/DOCX**.

> ⚠️ **Disclaimer**: This is not legal advice. FIR formats can vary by jurisdiction. Always review the generated draft with the duty officer and follow the official template.

## Features
- Clean, responsive UI (dark, modern).
- Rich form: complainant, jurisdiction, incident details, IPC sections, suspects, witnesses, loss, requested action.
- Live preview of the generated FIR.
- Export to PDF or DOCX.
- Jinja-based reusable FIR template.

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
