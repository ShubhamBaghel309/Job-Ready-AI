import streamlit as st
from langchain_groq import ChatGroq
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from bs4 import BeautifulSoup
import requests
from docx import Document
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import os
import json
from typing import Dict, List, Optional
from dotenv import load_dotenv
import numpy as np

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

class ResumeTailor:
    def __init__(self):
        """Initialize the ResumeTailor with necessary components."""
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
            
        self.llm = ChatGroq(
            model="llama-3.1-70b-versatile",
            groq_api_key=GROQ_API_KEY,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def extract_text_from_pdf(self, pdf_file) -> str:
        """Extract text content from a PDF file using PyPDF2."""
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    
    def extract_text_from_docx(self, docx_file) -> str:
        """Extract text content from a DOCX file."""
        doc = Document(docx_file)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    
    def parse_job_description(self, job_text: str, is_url: bool = True) -> Dict:
        """Extract job details from the provided URL or text."""
        if is_url:
            loader = WebBaseLoader(job_text)
            data = loader.load()
            job_content = data[0].page_content
        else:
            job_content = job_text
        
        # Use LLM to extract structured information
        prompt = f"""Please analyze the following job description and extract key information in JSON format.
        Return ONLY a JSON object with the following structure:
        {{
            "skills": ["skill1", "skill2", ...],
            "experience": "experience requirements",
            "responsibilities": ["responsibility1", "responsibility2", ...],
            "company": "company name",
            "title": "job title"
        }}

        Job Description:
        {job_content}
        """
        
        response = self.llm.invoke(prompt)
        try:
            # Extract content and clean it to ensure it's valid JSON
            content = str(response.content).strip()
            if content.startswith("```json"):
                content = content.split("```json")[1]
            if content.endswith("```"):
                content = content.rsplit("```", 1)[0]
            return json.loads(content.strip())
        except json.JSONDecodeError:
            # Fallback structure if parsing fails
            return {
                "skills": [],
                "experience": "Not specified",
                "responsibilities": [],
                "company": "Not specified",
                "title": "Not specified"
            }
    
    def match_skills(self, resume_text: str, job_requirements: Dict) -> Dict:
        """Match resume skills with job requirements using semantic similarity."""
        try:
            # Ensure skills is a list and not empty
            if not job_requirements.get('skills') or not isinstance(job_requirements['skills'], list):
                return {
                    'matched_skills': [],
                    'missing_skills': []
                }
            
            # Preprocess resume text to extract potential skills
            # Split into sentences and words to better match individual skills
            resume_words = ' '.join([word.strip() for word in resume_text.replace('\n', ' ').split()])
            
            # Convert resume text and skills into embeddings
            resume_embedding = self.embedding_model.encode(resume_words)
            job_skills_embeddings = self.embedding_model.encode(job_requirements['skills'])
            
            # Calculate cosine similarity
            similarities = resume_embedding @ job_skills_embeddings.T / (
                np.linalg.norm(resume_embedding) * np.linalg.norm(job_skills_embeddings, axis=1)
            )
            
            # Use a lower threshold for better matching
            threshold = 0.3
            
            matched_skills = []
            missing_skills = []
            
            for idx, skill in enumerate(job_requirements['skills']):
                if similarities[idx] > threshold:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)
            
            return {
                'matched_skills': matched_skills,
                'missing_skills': missing_skills
            }
        except Exception as e:
            st.error(f"Error in skill matching: {str(e)}")
            return {
                'matched_skills': [],
                'missing_skills': []
            }
    
    def tailor_resume(self, resume_text: str, job_requirements: Dict, skill_matches: Dict) -> Dict:
        """Generate a tailored resume using the LLM and provide improvement analysis."""
        # First, get the tailored resume content
        resume_prompt = f"""Rewrite the following resume to better match the job requirements. 
        Focus on quantifiable achievements and emphasize these matched skills: {skill_matches['matched_skills']}.
        Also, incorporate these missing but relevant skills if the candidate has related experience: {skill_matches['missing_skills']}.
        
        Original Resume:
        {resume_text}
        
        Job Requirements:
        {json.dumps(job_requirements, indent=2)}
        
        Return ONLY the tailored resume text, without any explanations or analysis.
        """
        
        tailored_resume = str(self.llm.invoke(resume_prompt).content)
        
        # Then, get the analysis separately
        analysis_prompt = f"""Analyze how the resume matches the job requirements and provide a detailed improvement analysis.
        Focus on these aspects:
        1. Skills alignment
        2. Experience relevance
        3. Achievement emphasis
        4. Missing keywords
        5. Suggested improvements
        
        Original Resume:
        {resume_text}
        
        Job Requirements:
        {json.dumps(job_requirements, indent=2)}
        
        Matched Skills: {skill_matches['matched_skills']}
        Missing Skills: {skill_matches['missing_skills']}
        
        Provide the analysis in JSON format with these keys:
        {{
          "improvements": ["list of specific improvements needed"],
          "skills_analysis": {{
              "matched": ["detailed explanation of how each matched skill aligns"],
              "missing": ["suggestions for addressing each missing skill"]
          }},
          "achievement_emphasis": ["list of quantifiable achievements that should be highlighted"],
          "keyword_optimization": ["key terms that should be added for ATS"]
        }}
        """
        
        analysis_response = self.llm.invoke(analysis_prompt)
        try:
            content = str(analysis_response.content).strip()
            if content.startswith("```json"):
                content = content.split("```json")[1]
            if content.endswith("```"):
                content = content.rsplit("```", 1)[0]
            analysis_result = json.loads(content.strip())
            analysis_result["tailored_resume"] = tailored_resume
            return analysis_result
        except json.JSONDecodeError:
            return {
                "improvements": ["Error analyzing improvements"],
                "skills_analysis": {"matched": [], "missing": []},
                "achievement_emphasis": [],
                "keyword_optimization": [],
                "tailored_resume": tailored_resume
            }
    
    def generate_docx(self, tailored_content: str) -> Document:
        """Convert the tailored content into a DOCX file."""
        doc = Document()
        # Only include the actual resume content, no analysis
        content = str(tailored_content).strip()
        for paragraph in content.split('\n'):
            if paragraph.strip():
                doc.add_paragraph(paragraph.strip())
        return doc
    
    def generate_cold_email(self, resume_text: str, job_requirements: Dict, skill_matches: Dict) -> str:
        """Generate a personalized cold email based on the resume and job requirements."""
        prompt = f"""Generate a professional cold email for a job application based on the following information.
        The email should:
        1. Be concise and professional
        2. Highlight key matching skills: {skill_matches['matched_skills']}
        3. Reference specific job requirements
        4. Include a brief mention of relevant achievements
        5. End with a call to action
        
        Job Details:
        Company: {job_requirements.get('company', 'the company')}
        Position: {job_requirements.get('title', 'the position')}
        
        Resume Context:
        {resume_text[:500]}  # Using first 500 characters for context
        
        Format the email with:
        - Professional subject line
        - Greeting
        - 2-3 concise paragraphs
        - Professional closing
        
        Return the complete email with subject line.
        """
        
        response = self.llm.invoke(prompt)
        return str(response.content)

def main():
    st.set_page_config(layout="wide")  # Use wide layout for full screen
    
    # Center-aligned title with custom styling
    st.markdown("""
        <h1 style='text-align: center; color: #1E88E5; padding: 1rem;'>
            🎯 AI-Powered Resume Tailor
        </h1>
        <p style='text-align: center; color: #666; margin-bottom: 2rem;'>
            Optimize your resume for ATS using AI
        </p>
    """, unsafe_allow_html=True)
    
    try:
        # Initialize ResumeTailor
        tailor = ResumeTailor()
        
        # Create two main columns for the layout
        left_col, right_col = st.columns([1, 1.5], gap="large")  # Added gap between columns
        
        with left_col:
            st.header("📤 Upload Resume & Job Details")
            # File upload
            resume_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=['pdf', 'docx'])
            
            # Job input method selection
            job_input_method = st.radio(
                "Choose how to input the job description:",
                ["Enter URL", "Paste Description"]
            )
            
            job_text = ""
            is_url = True
            
            if job_input_method == "Enter URL":
                job_text = st.text_input("Enter the job posting URL:")
                is_url = True
            else:
                job_text = st.text_area("Paste the job description here:", height=300)
                is_url = False
            
            if resume_file and job_text:
                process_button = st.button("🎯 Tailor Resume", use_container_width=True)
            else:
                st.info("Please upload your resume and provide job details to proceed.")
                process_button = False
        
        with right_col:
            if resume_file and job_text and process_button:
                with st.spinner("Processing your resume..."):
                    # Extract resume text
                    if resume_file.type == "application/pdf":
                        resume_text = tailor.extract_text_from_pdf(resume_file)
                    else:
                        resume_text = tailor.extract_text_from_docx(resume_file)
                    
                    # Parse job description
                    job_requirements = tailor.parse_job_description(job_text, is_url)
                    
                    # Match skills
                    skill_matches = tailor.match_skills(resume_text, job_requirements)
                    
                    # Generate tailored resume with analysis
                    analysis_result = tailor.tailor_resume(resume_text, job_requirements, skill_matches)
                    
                    # Generate cold email
                    cold_email = tailor.generate_cold_email(resume_text, job_requirements, skill_matches)
                    
                    # Create tabs for different sections
                    tabs = st.tabs(["💡 Analysis", "📧 Cold Email", "📄 Resume Versions"])
                    
                    # Analysis Tab
                    with tabs[0]:
                        # Skills Analysis
                        st.subheader("🎯 Skills Analysis")
                        skill_cols = st.columns(2)
                        with skill_cols[0]:
                            st.write("✅ Matched Skills")
                            for idx, skill_analysis in enumerate(analysis_result['skills_analysis']['matched'], 1):
                                st.write(f"{idx}. {skill_analysis}")
                        with skill_cols[1]:
                            st.write("📝 Missing Skills & Suggestions")
                            for idx, skill_suggestion in enumerate(analysis_result['skills_analysis']['missing'], 1):
                                st.write(f"{idx}. {skill_suggestion}")
                        
                        # Improvements
                        st.subheader("🔄 Improvements Made")
                        for idx, improvement in enumerate(analysis_result['improvements'], 1):
                            st.write(f"{idx}. {improvement}")
                        
                        # Achievements
                        st.subheader("📊 Quantifiable Achievements")
                        for idx, achievement in enumerate(analysis_result['achievement_emphasis'], 1):
                            st.write(f"{idx}. {achievement}")
                        
                        # Keywords
                        st.subheader("🔍 ATS Keywords")
                        for idx, keyword in enumerate(analysis_result['keyword_optimization'], 1):
                            st.write(f"{idx}. {keyword}")
                    
                    # Cold Email Tab
                    with tabs[1]:
                        st.subheader("📧 Cold Email Template")
                        st.text_area("Copy the email below:", cold_email, height=400)
                    
                    # Resume Versions Tab
                    with tabs[2]:
                        st.subheader("📋 Compare Versions")
                        version_cols = st.columns(2)
                        with version_cols[0]:
                            st.write("Original Resume")
                            st.text_area("", resume_text, height=400, disabled=True)
                        with version_cols[1]:
                            st.write("Tailored Resume")
                            st.text_area("", analysis_result['tailored_resume'], height=400, disabled=True)
                        
                        # Download button
                        st.subheader("📥 Download")
                        doc = tailor.generate_docx(analysis_result['tailored_resume'])
                        doc.save("tailored_resume.docx")
                        
                        with open("tailored_resume.docx", "rb") as file:
                            st.download_button(
                                label="⬇️ Download Tailored Resume",
                                data=file,
                                file_name="tailored_resume.docx",
                                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                use_container_width=True
                            )
                
    except ValueError as e:
        st.error(f"Configuration Error: {str(e)}")
        st.info("Please ensure you have set up the GROQ_API_KEY in your .env file")

if __name__ == "__main__":
    main()
