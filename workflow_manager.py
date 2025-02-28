import streamlit as st
from typing import Optional
import tempfile

class WorkflowManager:
    """Manage app workflows and state transitions."""
    
    @staticmethod
    def handle_file_upload(file_types: list) -> Optional[str]:
        """Handle file upload with error checking."""
        try:
            uploaded_file = st.file_uploader("Upload your resume", type=file_types)
            if uploaded_file:
                file_type = uploaded_file.type
                if "pdf" in file_types and file_type == "application/pdf":
                    from PyPDF2 import PdfReader
                    reader = PdfReader(uploaded_file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text()
                    return text
                elif "docx" in file_types and file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    from docx import Document
                    doc = Document(uploaded_file)
                    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
                    return text
            return None
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            return None
    
    @staticmethod
    def handle_job_input() -> tuple[Optional[str], bool]:
        """Handle job description input."""
        job_input_method = st.radio(
            "Choose how to input the job description:",
            ["Enter URL", "Paste Description"]
        )
        
        is_url = job_input_method == "Enter URL"
        if is_url:
            job_text = st.text_input("Enter the job posting URL:")
        else:
            job_text = st.text_area("Paste the job description:", height=300)
        
        return job_text, is_url
    
    @staticmethod
    def show_success_message(message: str, duration: int = 3):
        """Show a success message that automatically disappears."""
        placeholder = st.empty()
        placeholder.success(message)
        if duration > 0:
            import time
            time.sleep(duration)
            placeholder.empty()
