# AI-Powered Resume Tailor

An intelligent resume tailoring system that optimizes resumes for ATS using Llama 3.3 via Groq Cloud. The system focuses on quantifiable achievements and aligns your resume with job-specific requirements.

## Features

- Resume parsing (PDF/DOCX support)
- Job description analysis
- Skill matching using semantic similarity
- AI-powered resume tailoring
- ATS-friendly output in DOCX format
- Quantifiable achievement emphasis

## Prerequisites

- Python 3.8+
- Groq API key (sign up at https://console.groq.com)

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

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Enter your Groq API key

4. Upload your resume (PDF or DOCX format)

5. Provide the job posting URL

6. Click "Tailor Resume" to generate your optimized resume

## How It Works

1. **Resume Processing**: Extracts text content from your PDF/DOCX resume
2. **Job Analysis**: Parses the job posting to identify required skills and responsibilities
3. **Skill Matching**: Uses semantic matching to identify matching and missing skills
4. **Resume Tailoring**: Rewrites your resume to emphasize relevant skills and achievements
5. **Output**: Generates an ATS-friendly DOCX file

## Security Note

- Your Groq API key is handled securely and is never stored
- All processing is done in real-time
- No data is permanently stored on servers

## License

MIT License 