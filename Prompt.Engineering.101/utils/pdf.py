from fpdf import FPDF
import streamlit as st
import base64

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AI-Driven Prompt Engineering Curriculum Progress Report", ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_pdf_report(progress):
    pdf = PDFReport()
    pdf.add_page()
    for module, status in progress.items():
        pdf.chapter_title(module)
        pdf.chapter_body(f"Status: {status}")
    
    pdf_output = pdf.output(dest="S").encode("latin1")
    b64_pdf = base64.b64encode(pdf_output).decode("latin1")
    pdf_download_link = f'<a href="data:application/pdf;base64,{b64_pdf}" download="progress_report.pdf">Download Progress Report</a>'
    st.markdown(pdf_download_link, unsafe_allow_html=True)
