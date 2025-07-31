# 🎯 Job Ready AI- AI-Powered Job Application Suite

**Resume Tailor** is a comprehensive AI-powered platform that helps job seekers optimize their resumes, generate personalized cover letters, and analyze ATS compatibility. The platform features both a modern React frontend and a powerful Python backend with Streamlit support.

![Resume Tailor Banner](IMAGES/IMG1.png)
Live App="https://jobready.streamlit.app/"

## ✨ Features

### 🎯 Core Functionality
- **Resume Analysis & Optimization**: Upload your resume and get AI-powered suggestions for improvement
- **Job-Specific Tailoring**: Automatically adapt your resume to match specific job descriptions
- **ATS Score Analysis**: Get detailed scoring on how well your resume performs with Applicant Tracking Systems
- **Cover Letter Generation**: Create personalized cover letters based on your resume and job requirements
- **Cold Email Templates**: Generate professional networking emails for job opportunities

### 🔧 Powerful Backend
- **AI-Powered Analysis**: Uses Groq's LLaMA models for intelligent resume processing
- **Multiple File Formats**: Supports PDF and DOCX resume uploads
- **Web Scraping**: Can analyze job descriptions from URLs or direct text input
- **Semantic Matching**: Advanced skill matching using sentence transformers
- **Document Generation**: Export optimized resumes in multiple formats

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- **Python 3.8+**
- **LangChain** for LLM integration
- **Groq API** for AI processing
- **SentenceTransformers** for semantic analysis
- **PyPDF2 & python-docx** for document processing
- **Webbaseloader** for web scraping

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (3.8 or higher) - [Download here](https://python.org/)
- **Groq API Key** - [Get your key here](https://console.groq.com/)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ShubhamBaghel309/Job-Ready-AI.git
cd resume-tailor
```

### 2. Backend Setup (Python/Streamlit)

#### Install Python Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv myenv

# Activate virtual environment
# Windows:
myenv\Scripts\activate
# macOS/Linux:
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Optional: Other API keys
OPENAI_API_KEY=your_openai_key_here
```

#### Run the Streamlit Backend

```bash
# Start the Streamlit app
streamlit run main.py

# The app will be available at http://localhost:8501
```



#### Configure Frontend Environment

Create a `.env` file in the `frontend` directory:

```env
# API Configuration
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_NAME=Resume Tailor
```

#### Run the React Development Server

```bash
# Start the development server
npm run dev

# Or using yarn
yarn dev

# The frontend will be available at http://localhost:3000
```

## 🎮 How to Use

### Option 1: Streamlit Interface (Backend Only)

1. **Start the Application**:
   ```bash
   streamlit run main.py
   ```

2. **Choose Your Workflow**:
   - **Create New Resume**: Build a resume from scratch with AI guidance
   - **Tailor Existing Resume**: Optimize an existing resume for specific jobs

3. **Upload Your Resume**:
   - Drag and drop or browse for your PDF/DOCX resume file

4. **Provide Job Information**:
   - Paste a job description URL or enter the text directly

5. **Get Results**:
   - View your optimized resume
   - Check ATS compatibility score
   - Download cover letter and cold email templates

### Option 2: Modern React Frontend

1. **Start Both Servers**:
   ```bash
   # Terminal 1: Start backend
   streamlit run main.py
   
   # Terminal 2: Start frontend
   cd frontend && npm run dev
   ```

2. **Access the Application**:
   - Open your browser to `http://localhost:3000`
   - Enjoy the modern, responsive interface

3. **Use the Interface**:
   - Navigate through the beautiful UI
   - Upload resumes with drag-and-drop
   - View real-time progress and feedback
   - Download optimized documents

## 📁 Project Structure

```
resume-tailor/
├── 📁 backend/                 # Python backend files
│   ├── main.py                # Main Streamlit application
│   ├── resume_form.py         # Resume creation forms
│   ├── resume_generator.py    # Resume generation logic
│   ├── workflow_manager.py    # Workflow management
│   └── requirements.txt       # Python dependencies
├── 📁 frontend/               # React frontend
│   ├── 📁 src/
│   │   ├── 📁 components/     # Reusable UI components
│   │   ├── 📁 pages/          # Page components
│   │   ├── 📁 services/       # API service layer
│   │   ├── 📁 types/          # TypeScript definitions
│   │   ├── App.tsx            # Main app component
│   │   └── main.tsx           # Entry point
│   ├── package.json           # Node.js dependencies
│   └── vite.config.ts         # Vite configuration
├── 📁 templates/              # HTML templates
├── 📁 IMAGES/                 # Project images
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Development



#### Backend Scripts
```bash
# Run main application
streamlit run main.py

# Run with auto-reload
streamlit run main.py --server.runOnSave=true
```

## 🔐 API Configuration

### Groq API Setup

1. **Get Your API Key**:
   - Visit [Groq Console](https://console.groq.com/)
   - Sign up for an account
   - Navigate to API Keys section
   - Create a new API key

2. **Add to Environment**:
   ```bash
   # Add to your .env file
   GROQ_API_KEY=gsk_your_actual_api_key_here
   ```

3. **Verify Setup**:
   - The application will validate your API key on startup
   - You'll see an error message if the key is invalid

## 🎨 Customization

### Backend Templates

Resume templates can be customized in:

- `templates/resume_template.html` - HTML resume template
- Modify the template to change styling and layout

## 🐛 Troubleshooting

### Common Issues

1. **"GROQ_API_KEY not found"**
   ```bash
   # Solution: Check your .env file
   echo $GROQ_API_KEY  # Should show your key
   ```

3. **Module not found errors**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```


### Performance Tips

- Use a virtual environment for Python dependencies
- Consider using Redis for caching (advanced)


