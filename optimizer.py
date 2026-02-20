import pdfplumber
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
import os

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
                
    return text

def generate_pdf(text, output_path):
    doc = SimpleDocTemplate(output_path)
    styels = getSampleStyleSheet()
    elements = []
    
    for line in text.split("\n"):
        elements.append(Paragraph(line, styles["Normal"]))
        elements.append(Spacer(1, 0.2 * inch))
        
    doc.build(elements)
    
    
    
            
