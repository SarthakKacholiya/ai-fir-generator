import unittest
from generator.builder import generate_fir_text

class TestFIRBuilder(unittest.TestCase):
    def test_minimal_render(self):
        data = {
            "complainant_name": "Amit Sharma",
            "complainant_age": "31",
            "complainant_gender": "Male",
            "complainant_address": "MG Road, Jaipur",
            "complainant_phone": "9999999999",
            "complainant_email": "amit@example.com",
            "relation_to_victim": "Self",
            "police_station": "Vaishali Nagar PS",
            "district": "Jaipur",
            "state": "Rajasthan",
            "incident_datetime": "2025-08-28T19:30",
            "incident_place": "Near City Mall",
            "category": "Theft",
            "narrative": "On the stated date and time, my phone was snatched by two unknown persons on a motorcycle while I was walking near City Mall. I attempted to chase but failed. CCTV may be available at nearby shops.",
            "suspects": "Two unknown males on a black motorcycle, partial plate 'RJ14-AB-'.",
            "witnesses": "Security guard at City Mall; shopkeeper at Corner Store.",
            "loss_value": "Approx ₹45,000 (mobile phone).",
            "ipc_sections": "379 (Theft), 356 (Assault or criminal force).",
            "requested_action": "Register FIR, seize CCTV footage, track IMEI, investigate and recover property.",
            "signature_place": "Jaipur",
            "signature_date": "2025-08-29",
            "declaration_truth": True,
            "consent_contact": True,
        }
        txt = generate_fir_text(data)
        self.assertIn("FIRST INFORMATION REPORT", txt)
        self.assertIn("Amit Sharma", txt)
        self.assertIn("Vaishali Nagar PS", txt)

if __name__ == "__main__":
    unittest.main()
