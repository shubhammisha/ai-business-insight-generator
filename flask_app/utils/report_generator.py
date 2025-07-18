from fpdf import FPDF

def generate_pdf_report(insights: dict, output_path: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Business Insights Report', ln=True, align='C')
    pdf.ln(10)

    # Insights
    pdf.set_font('Arial', '', 12)
    for label, insight in insights.items():
        pdf.set_text_color(40, 40, 40)
        pdf.cell(0, 10, f"{label.replace('_', ' ').capitalize()}:", ln=True)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, f"{insight}")
        pdf.ln(2)

    pdf.output(output_path) 