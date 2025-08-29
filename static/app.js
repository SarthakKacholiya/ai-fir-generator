// Simple client-side validation hints
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("firForm");
  if (!form) return;
  form.addEventListener("submit", (e) => {
    const narrative = form.querySelector('textarea[name="narrative"]');
    const station = form.querySelector('input[name="police_station"]');
    const place = form.querySelector('input[name="incident_place"]');
    const dt = form.querySelector('input[name="incident_datetime"]');

    const errs = [];
    if (narrative && narrative.value.trim().length < 40) {
      errs.push("Narrative should be at least 40 characters for clarity.");
    }
    if (!station.value.trim()) errs.push("Police Station is required.");
    if (!place.value.trim()) errs.push("Place of occurrence is required.");
    if (!dt.value.trim()) errs.push("Incident date & time is required.");

    if (errs.length) {
      e.preventDefault();
      alert("Please fix:\n• " + errs.join("\n• "));
    }
  });
});
