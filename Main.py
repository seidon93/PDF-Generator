from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

pdf.add_page()
pdf.set_font('Arial', 'B', size=24)
pdf.cell(w=0, h=0, ln=1, align='C', txt='PDF Generator')

# Header
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=20)
    pdf.set_text_color(145, 0, 180)
    pdf.cell(w=0, h=15, ln=1,  txt=row["Topic"])
    pdf.line(10,22, 200, 22)


    pdf.ln(257)
    pdf.set_font('Helvetica', 'I', size=14)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=14, ln=1, align='R', txt=row["Topic"])


    # Footer
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font('Helvetica', 'I', size=14)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=14, ln=1, align='R', txt=row["Topic"])

pdf.output('output.pdf')

