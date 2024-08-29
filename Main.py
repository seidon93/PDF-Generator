from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

pdf.add_page()
pdf.set_font('Arial', 'B', size=24)
pdf.cell(w=0, h=0, ln=1, align='C', txt='PDF Generator')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=20)
    pdf.set_text_color(145, 0, 180)
    pdf.cell(w=0, h=15, ln=1,  txt=row["Topic"])
    pdf.line(10,22, 200, 22)
pdf.output('output.pdf')

