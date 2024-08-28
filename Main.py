from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.set_font('Arial', 'B', size=20)
pdf.cell(w=0, h=0, ln=1, align='C', txt='PDF Generator')
pdf.cell(w=0, h=15, ln=1)

pdf.set_font('Arial', 'B', size=16)
pdf.cell(w=0, h=16, ln=1, align='L', txt='Example text', border=1)

pdf.output('output.pdf')
