from fpdf import FPDF
import hello
import uuid

def create_pdf_report(algo, detail_df, df, body, img_buffer):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=20)
    pdf.cell(200, 10, txt=f"Algorithm Analysis : {algo}", ln=True, align="C")
    pdf.ln(10)
    # Add textual summary
    pdf.set_font("Helvetica", size=14)
    pdf.multi_cell(0, 10, "Characteristics :")
    pdf.ln(3)
    # Add table header
    pdf.set_font("Helvetica", size=12)
    pdf.cell(60, 10, "Attributes", 1)
    pdf.cell(135, 10, "Description", 1)
    pdf.ln()
    # Add table rows
    for _, row in detail_df.iterrows():
        pdf.cell(60, 10, row[0], 1)
        pdf.cell(135, 10, row[1], 1)
        pdf.ln()
    pdf.ln(10)
    # Add Source Code
    pdf.set_font("Helvetica", size=14)
    pdf.cell(0, 10, "Source Code :")
    pdf.ln(2)
    pdf.set_font("Courier", size=12)
    pdf.multi_cell(0, 7, txt=f"{body}")

    pdf.add_page()
    # Add table header for multiple array
    
    pdf.set_font("Helvetica", size=14)
    pdf.multi_cell(0, 10, "Analysis :")
    pdf.ln(4)
    pdf.set_font("Helvetica", size=12)
    for col in df.columns:
        pdf.cell(40, 10, str(col), 1)
    pdf.ln()
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, str(item), 1)
        pdf.ln()
    pdf.ln(10)

    pdf.image(img_buffer, w=150)
    img_buffer.close()

    return pdf.output(dest="S")
