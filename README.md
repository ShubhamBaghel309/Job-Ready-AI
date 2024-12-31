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