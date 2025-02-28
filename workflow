                        +---------------------------+
                        | User Interface (Streamlit)|
                        +---------------------------+
                                       |
                                       v
                        +-------------------------+
                        | Landing Page            |
                        | - Create New Resume     |
                        | - Tailor Existing Resume|
                        +-------------------------+
                                       |
                                       v
                        +-------------------------+
                        | Workflow Selection      |
                        | - Create New Resume     |
                        | - Tailor Existing Resume|
                        +-------------------------+
                                    |
        -----------------------------------------------       
        |                                              |
        v                                              v
+-------------------------+       +-------------------------+
| Create New Resume       |       | Tailor Existing Resume  |
+-------------------------+       +-------------------------+
        |                                |
        v                                v
+-------------------------+       +-------------------------+
| Form Steps              |       | Resume Upload           |
| - Personal Info         |       | - PDF/DOCX              |
| - Education             |       | Job Description URL     |
| - Experience            |       | - WebBaseLoader         |
| - Skills                |       | - BeautifulSoup         |
| - Review                |       +-------------------------+
+-------------------------+                |
        |                                   v
        v                        +-------------------------+
+-------------------------+      | Resume Parsing          |
| Generate Resume         |      | - pdfminer/python-docx  |
| - Format Data           |      +-------------------------+
| - Render HTML           |                |
| - Generate PDF          |                v
| - Show Preview          |      +-------------------------+
| - Download Options      |      | Structured Resume in JSON|
+-------------------------+      +-------------------------+
        |                                   |
        v                                   v
+-------------------------+      +-------------------------+
| Show Success Message    |      | Skill Matching          |
+-------------------------+      | - sentence_transformers |
                                 +-------------------------+
                                            |
                                            v
                                 +-------------------------+
                                 | Tailor Resume           |
                                 | - Llama 3.1, LangChain  |
                                 +-------------------------+
                                            |
                                            v
                                 +-------------------------+
                                 | Generate Cold Email     |
                                 |  and cover letter       |
                                 +-------------------------+
                                             |
                                 +----------------------------+
                                 | Download Tailored Resume   |
                                 | ,Cold Email and cover letter            |
                                 +----------------------------+