import os
import uuid
from flask import Flask, render_template, request, send_file, url_for
from generator.builder import generate_fir_text, build_docx, build_pdf

app = Flask(__name__)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    fir_text = None
    download_path = None

    if request.method == "POST":
        # Collect inputs safely
        data = {
            "complainant_name": request.form.get("complainant_name", "").strip(),
            "complainant_age": request.form.get("complainant_age", "").strip(),
            "complainant_gender": request.form.get("complainant_gender", "").strip(),
            "complainant_address": request.form.get("complainant_address", "").strip(),
            "complainant_phone": request.form.get("complainant_phone", "").strip(),
            "complainant_email": request.form.get("complainant_email", "").strip(),
            "relation_to_victim": request.form.get("relation_to_victim", "").strip(),
            "police_station": request.form.get("police_station", "").strip(),
            "district": request.form.get("district", "").strip(),
            "state": request.form.get("state", "").strip(),
            "incident_datetime": request.form.get("incident_datetime", "").strip(),
            "incident_place": request.form.get("incident_place", "").strip(),
            "category": request.form.get("category", "").strip(),
            "narrative": request.form.get("narrative", "").strip(),
            "suspects": request.form.get("suspects", "").strip(),
            "witnesses": request.form.get("witnesses", "").strip(),
            "loss_value": request.form.get("loss_value", "").strip(),
            "ipc_sections": request.form.get("ipc_sections", "").strip(),
            "requested_action": request.form.get("requested_action", "").strip(),
            "signature_place": request.form.get("signature_place", "").strip(),
            "signature_date": request.form.get("signature_date", "").strip(),
            "declaration_truth": bool(request.form.get("declaration_truth")),
            "consent_contact": bool(request.form.get("consent_contact")),
        }

        fir_text = generate_fir_text(data)

        fmt = request.form.get("format_type", "pdf")
        filename = f"{uuid.uuid4()}"
        if fmt == "docx":
            out_path = os.path.join(OUTPUT_DIR, f"{filename}.docx")
            build_docx(fir_text, out_path)
        else:
            out_path = os.path.join(OUTPUT_DIR, f"{filename}.pdf")
            build_pdf(fir_text, out_path)

        download_path = out_path

    return render_template(
        "index.html",
        fir_text=fir_text,
        download_url=(url_for("download", filepath=download_path) if download_path else None),
    )

@app.route("/download")
def download():
    filepath = request.args.get("filepath")
    if not filepath or not os.path.exists(filepath):
        return "File not found", 404
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
