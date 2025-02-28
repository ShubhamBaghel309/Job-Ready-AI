# AI-Powered Resume Tailor 🎯

An intelligent resume optimization tool that helps tailor your resume for specific job applications using AI. The application analyzes job descriptions, matches skills, and provides personalized improvements to increase your chances of getting through Applicant Tracking Systems (ATS).

## Features 🌟

- **Resume Analysis**: Comprehensive analysis of your resume against job requirements
- **ATS Score Optimization**: Calculates and improves your resume's ATS compatibility score
- **Skill Matching**: Identifies matched and missing skills from job requirements
- **Smart Content Tailoring**: Optimizes resume content while maintaining authenticity
- **Professional Documents**: Generates tailored resumes, cover letters, and cold emails
- **PDF Generation**: Creates professionally formatted PDF resumes using a clean template
- **Session Persistence**: Maintains all generated content throughout your session

## Prerequisites 📋

1. Python 3.7+
2. wkhtmltopdf (for PDF generation)
   - Windows: Download from https://wkhtmltopdf.org/downloads.html
   - Mac: `brew install wkhtmltopdf`
   - Linux: `sudo apt-get install wkhtmltopdf`
3. Groq API key (sign up at https://console.groq.com)

## Installation 🚀

1. Clone the repository:
```bash
git clone <repository-url>
cd resume-tailor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_api_key_here
```

## Usage 💡

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Access the application at `http://localhost:8000`

3. Upload your resume (PDF/DOCX format)

4. Provide job description (URL or text)

5. Click "Tailor Resume" to generate:
   - ATS Score Analysis
   - Skill Match Analysis
   - Improvement Suggestions
   - Tailored Resume
   - Cover Letter
   - Cold Email

## Technical Details 🔧

### Dependencies
- `streamlit`: Web application framework
- `langchain_groq`: LLM integration
- `sentence_transformers`: Semantic text analysis
- `beautifulsoup4`: HTML parsing
- `PyPDF2`: PDF processing
- `python-docx`: DOCX processing
- `pdfkit`: PDF generation
- See `requirements.txt` for complete list

### Key Components

1. **Resume Processing**:
   - Text extraction from PDF/DOCX
   - Section identification
   - Content structuring

2. **Job Analysis**:
   - Web scraping (URL input)
   - Text processing
   - Requirement extraction
   - Skill identification

3. **Skill Matching**:
   - Direct keyword matching
   - Semantic similarity analysis
   - Technical variation handling
   - Context-aware matching

4. **Content Generation**:
   - Resume optimization
   - Cover letter generation
   - Cold email creation
   - PDF formatting

5. **ATS Scoring**:
   - Keyword analysis
   - Format checking
   - Content relevance
   - Section scoring

### File Structure
```
resume-tailor/
├── main.py              # Main application code
├── requirements.txt     # Python dependencies
├── template.html        # Resume template
├── .env                # Environment variables
└── README.md           # Documentation
```

## Best Practices 📝

1. **Resume Format**:
   - Use standard section headers
   - Include quantifiable achievements
   - Maintain consistent formatting
   - Use industry-standard terminology

2. **Job Description**:
   - Provide complete job descriptions
   - Include all requirements
   - Specify technical skills clearly

3. **PDF Generation**:
   - Ensure wkhtmltopdf is properly installed
   - Keep template formatting clean
   - Verify PDF output quality

## Troubleshooting 🔍

1. **PDF Generation Issues**:
   - Verify wkhtmltopdf installation
   - Check system PATH configuration
   - Ensure template.html exists

2. **API Errors**:
   - Verify Groq API key in .env
   - Check internet connection
   - Monitor API rate limits

3. **Content Processing**:
   - Use supported file formats
   - Keep file sizes under 5MB
   - Ensure clean formatting

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Groq for LLM API
- Streamlit for the web framework
- wkhtmltopdf for PDF generation
- All open-source contributors

## Contact 📧

For support or queries, please open an issue in the repository.

---
Made with ❤️ using AI and Python

