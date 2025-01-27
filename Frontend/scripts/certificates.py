from fpdf import FPDF

class CertificateGenerator:
    def __init__(self):
        pass

    def generate_certificate(self, name, course):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=20)
        pdf.cell(200, 10, txt="Certificate of Completion", ln=True, align='C')
        pdf.ln(20)
        pdf.set_font("Arial", size=14)
        pdf.cell(200, 10, txt=f"This certifies that {name}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"has successfully completed the course '{course}'", ln=True, align='C')
        pdf.output(f"{name}_certificate.pdf")
        return f"{name}_certificate.pdf has been created!"

# Example Usage
if __name__ == "__main__":
    cg = CertificateGenerator()
    cg.generate_certificate("Alice", "Python Programming")
