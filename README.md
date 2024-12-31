
# AI-Powered Resume Tailor

An intelligent resume optimization system that enhances resumes for ATS (Applicant Tracking Systems) using advanced AI techniques. The system provides comprehensive analysis, scoring, and improvement suggestions to maximize your chances of getting past ATS filters.

## Key Features

### 1. Resume Analysis & Optimization
- PDF and DOCX file support
- Intelligent text extraction and parsing
- Job description analysis and requirement extraction
- Smart skill matching with semantic understanding
- ATS-optimized resume generation
- Before/After comparison

### 2. Advanced Skill Matching
- Semantic similarity analysis
- Technical term variation handling (e.g., "ML" ↔ "Machine Learning")
- Context-aware skill detection
- Explicit and implicit skill matching
- Detailed skill gap analysis

### 3. ATS Scoring System
- Comprehensive scoring algorithm using TF-IDF and cosine similarity
- Section-wise scoring breakdown:
  - Keyword Match (30 points)
  - Experience Alignment (25 points)
  - Skills Match (25 points)
  - Education Relevance (10 points)
  - Format & Organization (10 points)
- Before/After score comparison
- Improvement percentage calculation

### 4. Detailed Analytics
- Skills gap analysis
- Keyword density metrics
- Section-by-section scoring
- Quantifiable achievements extraction
- Format and structure analysis

### 5. Improvement Suggestions
- Actionable improvement recommendations
- Keyword optimization suggestions
- Format enhancement tips
- Section-specific improvements
- Achievement emphasis guidance

### 6. Professional Cold Email Generation
- Context-aware email drafting
- Skill-focused content
- Professional formatting
- Customized to job requirements
- Call-to-action inclusion

### 7. Document Management
- Side-by-side version comparison
- DOCX format export
- Original resume preservation
- Clean formatting maintenance
- ATS-friendly output

## Technical Features
- Semantic text analysis using NLTK
- TF-IDF vectorization for content comparison
- Cosine similarity for matching accuracy
- LLM integration via Groq
- Streamlit-based interactive UI

## Prerequisites

- Python 3.8+
- Groq API key (sign up at https://console.groq.com)
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/resume-tailor.git
cd resume-tailor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Upload your resume (PDF or DOCX format)

3. Provide job description (URL or text)

4. Click "Tailor Resume" to generate:
   - ATS Score Analysis
   - Optimized Resume
   - Improvement Suggestions
   - Professional Cold Email

## How It Works

1. **Resume Processing**:
   - Text extraction from PDF/DOCX
   - Content normalization
   - Structure analysis

2. **Job Analysis**:
   - Requirement extraction
   - Skill identification
   - Experience mapping

3. **Skill Matching**:
   - Direct keyword matching
   - Semantic similarity analysis
   - Technical variation handling

4. **ATS Scoring**:
   - TF-IDF vectorization
   - Cosine similarity calculation
   - Multi-factor scoring

5. **Resume Optimization**:
   - Keyword integration
   - Format enhancement
   - Content restructuring

6. **Output Generation**:
   - DOCX file creation
   - Cold email drafting
   - Analysis report compilation

## Security

- Groq API key is handled securely
- No data storage on servers
- Local file processing only
- Secure document handling

## License

MIT License 
=======
# Resume Tailor
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
   git clone https://github.com/ShubhamBaghel309/TailorAI.git
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

