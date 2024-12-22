# TAILOR AI 
## Overview
This project provides an AI-powered tool to optimize resumes  and boost resume score for surpassing Applicant Tracking Systems (ATS) using advanced language models. It allows users to upload their resumes and job descriptions, tailoring the resume to better match job requirements. 

## Features
- **Resume Upload**: Supports PDF and DOCX formats.
- **Job Description Input**: Users can input job descriptions via URL or text.
- **Skill Matching**: Matches resume skills with job requirements using semantic similarity.
- **Tailored Resume Generation**: Generates a resume that emphasizes relevant skills and achievements.
- **Cold Email Generation**: Creates a professional email template for job applications.
- **Improvements Analysis**: Provides detailed analysis of how the resume aligns with job requirements and suggests specific improvements.
- **Downloadable Resume**: Allows users to download the tailored resume in DOCX format.

## Requirements
- Python 3.7+
- Streamlit
- Langchain
- PyPDF2
- Sentence Transformers
- python-dotenv

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your `GROQ_API_KEY`:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

# Workflow for AI-Powered Resume Tailor

## Overview
This document outlines the workflow for using the AI-Powered Resume Tailor application, detailing the steps from uploading a resume to generating a tailored document and cold email.

## Workflow Steps

1. **Start the Application**
   - Run the application using Streamlit:
     ```bash
     streamlit run main.py
     ```

2. **Upload Resume**
   - Navigate to the "Upload Resume & Job Details" section.
   - Click on the file uploader to upload your resume in either PDF or DOCX format.

3. **Input Job Description**
   - Choose how to input the job description:
     - **Enter URL**: Input the URL of the job posting.
     - **Paste Description**: Paste the job description directly into the text area.

4. **Process Resume and Job Description**
   - Ensure both the resume and job description are provided.
   - Click the "Tailor Resume" button to initiate processing.
   - The application will:
     - Extract text from the uploaded resume.
     - Parse the job description to identify key requirements.
     - Match skills from the resume with the job requirements.

5. **Receive Tailored Resume and Analysis**
   - The application will generate:
     - A tailored resume that emphasizes relevant skills and achievements.
     - An analysis of how the resume aligns with the job requirements, including:
       - Matched skills
       - Missing skills and suggestions for improvement
       - Quantifiable achievements to highlight
       - Keywords for ATS optimization

6. **Generate Cold Email**
   - A professional cold email template will be created based on the resume and job requirements.
   - The email will include:
     - Key matching skills
     - References to specific job requirements
     - A brief mention of relevant achievements
     - A call to action

7. **Review and Download**
   - Navigate through the tabs to review:
     - Skills Analysis
     - Cold Email Template
     - Comparison of Original and Tailored Resume
   - Download the tailored resume in DOCX format by clicking the download button.

8. **End of Workflow**
   - After reviewing and downloading, the user can close the application.

## Conclusion
This workflow provides a structured approach to using the AI-Powered Resume Tailor, ensuring users can effectively optimize their resumes and generate professional communication for job applications.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
