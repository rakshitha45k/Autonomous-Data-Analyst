from fpdf import FPDF

def generate_pdf_report(summary, insights, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "📊 Data Analysis Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.cell(0, 10, "Summary:", ln=True)

    for key, value in summary.items():
        pdf.cell(0, 8, f"- {key}: {value}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Insights:", ln=True)

    pdf.set_font("Arial", size=12)
    for i in insights:
        pdf.multi_cell(0, 8, f"- {i}")

    pdf.output(filename)
    return filename
