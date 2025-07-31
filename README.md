# Resume Tailor - AI-Powered Resume Optimizer

🎯 **Resume Tailor** is an intelligent resume optimization tool that uses AI to help you create ATS-friendly resumes tailored for specific job positions. It analyzes job descriptions, matches your skills, and generates optimized resumes with detailed scoring and suggestions.

## ✨ Features

### 🔄 Two Main Workflows
- **Create New Resume**: Build a professional resume from scratch with AI guidance
- **Tailor Existing Resume**: Optimize your current resume for specific job applications

### 🎯 Core Capabilities
- **Smart File Upload**: Support for PDF and DOCX resume formats
- **Job Description Analysis**: Parse job requirements from URLs or direct text input
- **AI-Powered Skill Matching**: Semantic analysis to match your skills with job requirements
- **ATS Score Analysis**: Comprehensive scoring across 5 key areas (100-point scale)
- **Resume Optimization**: Generate tailored resumes with improved keyword density
- **Cover Letter Generation**: Create personalized cover letters for each application
- **Cold Email Creation**: Generate professional outreach emails
- **Document Export**: Download optimized resumes in DOCX format

### 📊 ATS Scoring System
- **Keyword Match** (30 points): Exact matches with job requirements
- **Experience Alignment** (25 points): Relevance to required experience
- **Skills Match** (25 points): Technical and soft skills alignment
- **Education Relevance** (10 points): Educational background matching
- **Format & Organization** (10 points): Resume structure and readability

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- GROQ API key (for AI functionality)

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <your-repo-url>
   cd RESUMETAILOR
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   # On Windows:
   myenv\Scripts\activate
   # On macOS/Linux:
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run main.py
   ```

6. **Access the app**
   Open your browser and go to `http://localhost:8501`

## 💻 Usage Guide

### Creating a New Resume
1. Click "Start New Resume" on the landing page
2. Fill out the multi-step form with your information:
   - Personal Information
   - Education Details
   - Work Experience
   - Skills (Technical & Soft)
   - Review & Generate
3. Preview and download your generated resume

### Tailoring an Existing Resume
1. Click "Tailor Existing Resume" on the landing page
2. Upload your current resume (PDF or DOCX)
3. Provide job details:
   - Paste job description URL, or
   - Enter job description text directly
4. Click "Tailor Resume" to process
5. Review results in organized tabs:
   - **Analysis**: Skills matching and improvements
   - **ATS Score**: Before/after scoring with detailed breakdown
   - **Cold Email**: Generated outreach email
   - **Cover Letter**: Personalized cover letter
   - **Resume Versions**: Original vs. optimized comparison

## 📁 Project Structure

```
RESUMETAILOR/
├── main.py                 # Main Streamlit application
├── resume_form.py          # Form handling for new resume creation
├── resume_generator.py     # Resume generation and formatting
├── workflow_manager.py     # Workflow management utilities
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── templates/             # HTML templates for resume generation
├── myenv/                 # Virtual environment (auto-created)
└── frontend/              # React frontend (optional, separate)
```

## 🛠️ Key Dependencies

- **streamlit**: Web application framework
- **langchain-groq**: AI/LLM integration via GROQ
- **sentence-transformers**: Semantic similarity matching
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX file handling
- **beautifulsoup4**: Web scraping for job descriptions
- **numpy & pandas**: Data processing
- **python-dotenv**: Environment variable management

## ⚙️ Configuration

### Environment Variables
```env
GROQ_API_KEY=your_api_key_here
```

### API Keys Setup
1. Get a GROQ API key from [console.groq.com](https://console.groq.com)
2. Add it to your `.env` file
3. The app will automatically load it on startup

## 🎯 How It Works

1. **Resume Upload**: Extracts text from PDF/DOCX files
2. **Job Analysis**: Parses job descriptions using web scraping or direct input
3. **Skill Matching**: Uses semantic similarity to match resume skills with job requirements
4. **AI Optimization**: Leverages GROQ's Llama model to rewrite and optimize content
5. **ATS Scoring**: Analyzes multiple factors to provide comprehensive scoring
6. **Document Generation**: Creates downloadable optimized resumes

## 🔧 Troubleshooting

### Common Issues
- **GROQ API Key Error**: Ensure your API key is correctly set in the `.env` file
- **File Upload Issues**: Check that your resume is in PDF or DOCX format
- **Dependency Errors**: Make sure all packages are installed: `pip install -r requirements.txt`
- **Streamlit Issues**: Try running with: `streamlit run main.py --server.port 8501`

### Performance Tips
- Use clear, well-formatted resumes for better text extraction
- Provide detailed job descriptions for more accurate matching
- Keep job descriptions focused on key requirements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

## 📞 Support

For issues, questions, or feature requests:
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review the code documentation in the source files

---

**Built with Python, Streamlit, and AI** 🚀
