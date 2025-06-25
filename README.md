# 🎯 Job Ready AI - AI-Powered Resume Builder & Optimizer

RESUMETAILOR is a comprehensive AI-powered application designed to create, customize, and optimize resumes for specific job positions. Leveraging advanced natural language processing and machine learning techniques, the tool helps job seekers maximize their chances of success by tailoring their resumes to pass Applicant Tracking Systems (ATS) and appeal to hiring managers.

![RESUMETAILOR Banner](https://via.placeholder.com/800x200?text=RESUMETAILOR)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [Resume Analysis & Optimization](#resume-analysis--optimization)
  - [Multiple Document Formats](#multiple-document-formats)
  - [AI-Powered Content Generation](#ai-powered-content-generation)
  - [Interactive UI Features](#interactive-ui-features)
  - [Professional Templates](#professional-templates)
  - [Technical Features](#technical-features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Creating a New Resume](#creating-a-new-resume)
  - [Tailoring an Existing Resume](#tailoring-an-existing-resume)
  - [Working with Different Output Formats](#working-with-different-output-formats)
- [API Integration](#api-integration)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🔍 Overview

RESUMETAILOR offers a dual-purpose solution: it helps users create professional resumes from scratch and optimizes existing resumes for specific job opportunities. The application analyzes job descriptions, matches them with resume content, and provides detailed recommendations to improve ATS scores and overall resume effectiveness.

## ✨ Features

### Resume Analysis & Optimization

#### ATS Scoring System
- **Comprehensive Scoring**: Evaluates resumes across five key categories (Keyword Match, Experience Alignment, Skills Match, Education Relevance, Format & Organization)
- **Real-time Score Comparison**: Side-by-side before/after optimization scores with percentage improvement calculation
- **Detailed Analysis**: Section-by-section breakdown with specific improvement recommendations

#### Skills Matching
- **Semantic Similarity**: Uses SentenceTransformer embeddings to detect skill matches beyond exact keyword matching
- **Technical Variation Detection**: Recognizes common variations of technical terms (e.g., "JavaScript" and "JS")
- **Gap Analysis**: Automatically identifies missing skills required in the job description

#### Keyword Optimization
- **Density Analysis**: Calculates and visualizes keyword frequency in both original and optimized resumes
- **Strategic Placement**: Suggests optimal positioning of keywords for maximum ATS impact
- **Industry-specific Terminology**: Incorporates relevant industry terms based on job requirements

### Multiple Document Formats

#### Input Support
- **PDF Processing**: Extracts and analyzes text content from PDF resumes
- **DOCX Handling**: Parses Microsoft Word documents while preserving structure
- **Plain Text Input**: Direct text entry for maximum flexibility

#### Output Formats
- **Professional PDF Generation**: Creates polished, ATS-friendly PDF documents
- **Formatted DOCX Files**: Produces Microsoft Word documents with proper formatting
- **HTML Resume Version**: Generates web-ready HTML resumes with responsive design
- **LaTeX Support**: Creates LaTeX-based resumes for academic and technical positions

### AI-Powered Content Generation

#### Resume Tailoring
- **Job Description Analysis**: Automatically extracts key requirements, skills, and responsibilities
- **ATS Optimization**: Strategically incorporates keywords and phrases to increase ATS scores
- **Achievement Quantification**: Enhances impact by adding metrics and results to accomplishments

#### Cover Letter Generation
- **Automated Personalization**: Creates customized cover letters based on resume and job details
- **Job-specific Content**: Highlights relevant skills and experiences that match the position
- **Professional Formatting**: Follows standard business letter conventions with proper structure

#### Cold Email Creation
- **Customized Templates**: Generates concise, impactful cold emails for job applications
- **Skill Highlighting**: Features the most relevant skills matching the job requirements
- **Professional Tone**: Maintains appropriate formality and communication style

### Interactive UI Features

#### Progress Tracking
- **Multi-step Form Navigation**: Guided, step-by-step interface for resume creation
- **Visual Progress Indicators**: Clear display of current position in the workflow
- **Session State Management**: Preserves user data between steps and sessions

#### Real-time Preview
- **Side-by-side Comparison**: View original and optimized versions simultaneously
- **Live Content Updates**: Immediately see changes as you update information
- **Mobile-responsive Design**: Works seamlessly across devices of all sizes

#### Data Visualization
- **ATS Score Charts**: Graphical representation of score improvements
- **Skill Match Visualization**: Visual breakdown of matched vs. missing skills
- **Keyword Density Graphs**: Distribution analysis of key terms in the resume

### Professional Templates

#### Resume Templates
- **Multiple Layout Options**: Various professional designs to choose from
- **ATS-friendly Designs**: Templates optimized for machine readability
- **Customizable Sections**: Flexible component arrangement based on needs

#### Formatting Tools
- **Consistent Styling**: Maintains professional typography and spacing
- **High-contrast Design**: Enhanced readability for both humans and ATS systems
- **Proper Margins & Spacing**: Industry-standard document formatting

### Technical Features

#### AI Integration
- **Groq LLM Integration**: Leverages high-performance language models for content generation
- **Transformer-based Embeddings**: Uses cutting-edge semantic understanding for skill matching
- **Natural Language Processing**: Analyzes job descriptions and resumes for meaningful insights

#### Data Processing
- **JSON Handling**: Structured data management between components
- **Text Extraction & Parsing**: Sophisticated document content extraction
- **Document Conversion**: Seamless transformation between document formats

#### Security
- **Environment Variable Protection**: Secure API key management
- **Secure File Handling**: Temporary file creation with proper cleanup
- **Data Privacy**: Local processing where possible to maintain confidentiality

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) (for PDF generation)
- LaTeX installation (for LaTeX document generation)
- Groq API key (for AI functionality)
- Minimum 4GB RAM
- Internet connection for API calls

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RESUMETAILOR.git
   cd RESUMETAILOR
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install wkhtmltopdf:
   - Windows: Download and run the installer from the [official website](https://wkhtmltopdf.org/downloads.html)
   - macOS: `brew install wkhtmltopdf`
   - Linux: `sudo apt-get install wkhtmltopdf`

5. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Groq API key: `GROQ_API_KEY=your_api_key_here`

6. Verify installation:
   ```bash
   python -c "import pdfkit; print('PDF kit installed correctly')"
   wkhtmltopdf --version
   ```

## 🚀 Usage

### Creating a New Resume

1. Start the application:
   ```bash
   streamlit run main.py
   ```

2. Select "Create New Resume" on the landing page

3. Follow the step-by-step form to input your information:
   - Personal information
   - Education history
   - Work experience
   - Skills and certifications

4. Review your information and generate your resume

5. Download your resume in your preferred format (PDF, DOCX, or HTML)

### Tailoring an Existing Resume

1. Start the application and select "Tailor Existing Resume"

2. Upload your current resume (PDF or DOCX)

3. Provide the job description by either:
   - Entering the URL of the job posting
   - Pasting the job description text

4. Click "Tailor Resume" and wait for the analysis to complete

5. Review the results across the different tabs:
   - Analysis: See matched skills and suggested improvements
   - ATS Score: Compare before/after scores and section-by-section improvements
   - Cold Email: Get a ready-to-use email template for your application
   - Cover Letter: Download a customized cover letter
   - Resume Versions: Compare original and optimized resumes

6. Download the optimized resume in your preferred format

### Working with Different Output Formats

#### PDF Format
- Best for final submission to employers
- Generated with proper formatting and styling
- ATS-friendly with text extraction capabilities

#### DOCX Format
- Ideal for further manual editing
- Maintains structured sections with proper formatting
- Compatible with Microsoft Word and similar applications

#### HTML Format
- Perfect for online portfolios or websites
- Responsive design works across devices
- Can be directly integrated into web applications

#### LaTeX Format
- Specialized format for academic or technical positions
- Professional typesetting with mathematical formula support
- Highly customizable through LaTeX engine

## 🔌 API Integration

RESUMETAILOR uses the following APIs:

1. **Groq API**
   - Used for AI-powered text generation and analysis
   - Requires API key set in the .env file
   - Configuration in main.py through LangChain integration

2. **SentenceTransformers**
   - Used for semantic similarity matching
   - No API key required (runs locally)
   - Customizable embedding models available

## 🧰 Technologies Used

### Frontend
- **Streamlit**: Primary UI framework
- **HTML/CSS**: Custom styling and templates
- **Streamlit Components**: Enhanced UI elements
- **Lottie Animations**: Interactive loading animations

### Backend
- **Python 3.x**: Core programming language
- **LangChain**: Framework for LLM application development
- **Groq API**: Large language model provider
- **SentenceTransformers**: Embeddings for semantic matching

### Document Processing
- **PyPDF2**: PDF parsing and text extraction
- **python-docx**: Word document creation and parsing
- **LaTeX**: Academic and technical document generation
- **pdfkit/wkhtmltopdf**: HTML to PDF conversion

### AI/ML
- **Natural Language Processing**: Text analysis and understanding
- **Semantic Similarity Matching**: Comparing resume skills with job requirements
- **Large Language Models**: Content generation and optimization

### Data Handling
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing for similarity calculations
- **JSON Processing**: Structured data management

### Development Tools
- **Environment Management**: dotenv for configuration
- **Version Control**: Git for code management
- **Error Handling**: Robust exception management

## 📁 Project Structure

```
RESUMETAILOR/
├── main.py                 # Main application entry point
├── main2.py                # Secondary application implementation
├── main3.py                # Minimal implementation for testing
├── main4.py                # Enhanced UI implementation
├── latex_generator.py      # LaTeX resume generation functionality
├── latex_app.py            # LaTeX-specific UI
├── resume_form.py          # Form handling for resume creation
├── resume_generator.py     # Core resume generation functionality
├── workflow_manager.py     # Manages application workflow and state
├── latex.tex               # LaTeX template
├── requirements.txt        # Python dependencies
├── INSTALL.md              # Installation instructions
├── templates/              # HTML and document templates
│   └── resume_template.html  # HTML resume template
├── .env                    # Environment variables (not tracked)
└── README.md               # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- LaTeX resume template based on Jake Gutierrez's design
- SentenceTransformer models by UKPLab
- Streamlit for the interactive UI framework
- Groq for providing the LLM API

---

Built with ❤️ using Python and AI
