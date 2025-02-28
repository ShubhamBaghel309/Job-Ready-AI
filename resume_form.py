import streamlit as st
from typing import Dict, List
import re

class ResumeForm:
    """Handle the interactive resume creation form."""
    
    @staticmethod
    def initialize_form_state():
        """Initialize session state for form data if not exists."""
        if 'form_step' not in st.session_state:
            st.session_state.form_step = 1
        
        if 'form_data' not in st.session_state:
            st.session_state.form_data = {
                'personal_info': {},
                'education': [],
                'experience': [],
                'skills': {'technical': [], 'soft': []},
                'certifications': []
            }
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number format."""
        pattern = r'^\+?1?\d{9,15}$'
        return bool(re.match(pattern, phone))
    
    def render_progress_bar(self):
        """Render form progress indicator."""
        if 'form_step' not in st.session_state:
            st.session_state.form_step = 1
            
        total_steps = 5
        progress = (st.session_state.form_step - 1) / (total_steps - 1)
        st.progress(progress)
        
        # Display step labels
        cols = st.columns(total_steps)
        steps = ['Personal', 'Education', 'Experience', 'Skills', 'Review']
        
        for i, (col, step) in enumerate(zip(cols, steps), 1):
            with col:
                if i < st.session_state.form_step:
                    st.markdown(f"✅ {step}")
                elif i == st.session_state.form_step:
                    st.markdown(f"**🔵 {step}**")
                else:
                    st.markdown(f"⚪ {step}")
    
    def personal_info_form(self):
        """Render personal information form."""
        st.subheader("Personal Information")
        
        # Get existing data
        data = st.session_state.form_data['personal_info']
        
        # Personal details form
        full_name = st.text_input("Full Name*", data.get('full_name', ''))
        email = st.text_input("Email*", data.get('email', ''))
        phone = st.text_input("Phone Number*", data.get('phone', ''))
        location = st.text_input("Location", data.get('location', ''))
        linkedin = st.text_input("LinkedIn Profile", data.get('linkedin', ''))
        summary = st.text_area("Professional Summary", data.get('summary', ''), height=150)
        
        # Validation
        is_valid = True
        if not full_name:
            st.error("Full name is required")
            is_valid = False
        if email and not self.validate_email(email):
            st.error("Please enter a valid email address")
            is_valid = False
        if phone and not self.validate_phone(phone):
            st.error("Please enter a valid phone number")
            is_valid = False
        
        if st.button("Next →"):
            if is_valid:
                # Save data
                st.session_state.form_data['personal_info'] = {
                    'full_name': full_name,
                    'email': email,
                    'phone': phone,
                    'location': location,
                    'linkedin': linkedin,
                    'summary': summary
                }
                st.session_state.form_step = 2
                st.rerun()
    
    def education_form(self):
        """Render education form."""
        st.subheader("Education")
        
        # Display existing education entries
        for i, edu in enumerate(st.session_state.form_data['education']):
            with st.expander(f"Education #{i+1}", expanded=False):
                st.write(f"Degree: {edu['degree']}")
                st.write(f"Institution: {edu['institution']}")
                st.write(f"Years: {edu['start_year']} - {edu['end_year']}")
                if st.button(f"Remove Entry #{i+1}"):
                    st.session_state.form_data['education'].pop(i)
                    st.rerun()
        
        # Add new education entry
        with st.expander("Add Education", expanded=True):
            degree = st.text_input("Degree/Certificate*", key="new_degree")
            institution = st.text_input("Institution*", key="new_institution")
            col1, col2 = st.columns(2)
            with col1:
                start_year = st.number_input("Start Year", min_value=1950, max_value=2024, value=2020)
            with col2:
                end_year = st.number_input("End Year", min_value=1950, max_value=2030, value=2024)
            
            if st.button("Add Education Entry"):
                if degree and institution:
                    st.session_state.form_data['education'].append({
                        'degree': degree,
                        'institution': institution,
                        'start_year': start_year,
                        'end_year': end_year
                    })
                    st.rerun()
                else:
                    st.error("Please fill in all required fields")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back"):
                st.session_state.form_step = 1
                st.rerun()
        with col2:
            if st.button("Next →"):
                if len(st.session_state.form_data['education']) > 0:
                    st.session_state.form_step = 3
                    st.rerun()
                else:
                    st.error("Please add at least one education entry")
    
    def experience_form(self):
        """Render work experience form."""
        st.subheader("Work Experience")
        
        # Display existing experience entries
        for i, exp in enumerate(st.session_state.form_data['experience']):
            with st.expander(f"Experience #{i+1}", expanded=False):
                st.write(f"Title: {exp['title']}")
                st.write(f"Company: {exp['company']}")
                st.write(f"Duration: {exp['start_date']} - {exp['end_date']}")
                if st.button(f"Remove Entry #{i+1}"):
                    st.session_state.form_data['experience'].pop(i)
                    st.rerun()
        
        # Add new experience entry
        with st.expander("Add Experience", expanded=True):
            title = st.text_input("Job Title*", key="new_title")
            company = st.text_input("Company*", key="new_company")
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.text_input("Start Date (MM/YYYY)*", key="new_start_date")
            with col2:
                end_date = st.text_input("End Date (MM/YYYY or Present)*", key="new_end_date")
            responsibilities = st.text_area("Responsibilities and Achievements*", 
                                         help="Use bullet points (•) for each point", 
                                         height=150,
                                         key="new_responsibilities")
            
            if st.button("Add Experience Entry"):
                if all([title, company, start_date, end_date, responsibilities]):
                    st.session_state.form_data['experience'].append({
                        'title': title,
                        'company': company,
                        'start_date': start_date,
                        'end_date': end_date,
                        'responsibilities': responsibilities.split('\n')
                    })
                    st.rerun()
                else:
                    st.error("Please fill in all required fields")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back"):
                st.session_state.form_step = 2
                st.rerun()
        with col2:
            if st.button("Next →"):
                if len(st.session_state.form_data['experience']) > 0:
                    st.session_state.form_step = 4
                    st.rerun()
                else:
                    st.error("Please add at least one experience entry")
    
    def skills_form(self):
        """Render skills form."""
        st.subheader("Skills")
        
        # Technical Skills
        st.write("Technical Skills")
        tech_skills = st.text_area(
            "Enter technical skills (one per line)",
            '\n'.join(st.session_state.form_data['skills']['technical']),
            height=150,
            help="Examples: Python, Java, Project Management, Data Analysis"
        )
        
        # Soft Skills
        st.write("Soft Skills")
        soft_skills = st.text_area(
            "Enter soft skills (one per line)",
            '\n'.join(st.session_state.form_data['skills']['soft']),
            height=150,
            help="Examples: Leadership, Communication, Problem Solving"
        )
        
        # Certifications
        st.subheader("Certifications (Optional)")
        for i, cert in enumerate(st.session_state.form_data['certifications']):
            with st.expander(f"Certification #{i+1}", expanded=False):
                st.write(f"Name: {cert['name']}")
                st.write(f"Issuer: {cert['issuer']}")
                st.write(f"Year: {cert['year']}")
                if st.button(f"Remove Certification #{i+1}"):
                    st.session_state.form_data['certifications'].pop(i)
                    st.rerun()
        
        with st.expander("Add Certification", expanded=True):
            cert_name = st.text_input("Certification Name", key="new_cert_name")
            cert_issuer = st.text_input("Issuing Organization", key="new_cert_issuer")
            cert_year = st.number_input("Year", min_value=1950, max_value=2024, value=2024, key="new_cert_year")
            
            if st.button("Add Certification"):
                if cert_name and cert_issuer:
                    st.session_state.form_data['certifications'].append({
                        'name': cert_name,
                        'issuer': cert_issuer,
                        'year': cert_year
                    })
                    st.rerun()
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back"):
                st.session_state.form_step = 3
                st.rerun()
        with col2:
            if st.button("Review →"):
                # Save skills
                st.session_state.form_data['skills']['technical'] = [s.strip() for s in tech_skills.split('\n') if s.strip()]
                st.session_state.form_data['skills']['soft'] = [s.strip() for s in soft_skills.split('\n') if s.strip()]
                
                if len(st.session_state.form_data['skills']['technical']) > 0:
                    st.session_state.form_step = 5
                    st.rerun()
                else:
                    st.error("Please add at least one technical skill")
    
    def review_form(self):
        """Render review page."""
        st.subheader("Review Your Information")
        
        data = st.session_state.form_data
        
        # Personal Information
        with st.expander("Personal Information", expanded=True):
            st.write(f"**Name:** {data['personal_info'].get('full_name')}")
            st.write(f"**Email:** {data['personal_info'].get('email')}")
            st.write(f"**Phone:** {data['personal_info'].get('phone')}")
            st.write(f"**Location:** {data['personal_info'].get('location')}")
            st.write(f"**LinkedIn:** {data['personal_info'].get('linkedin')}")
            st.write("**Summary:**")
            st.write(data['personal_info'].get('summary'))
        
        # Education
        with st.expander("Education", expanded=True):
            for edu in data['education']:
                st.write(f"**{edu['degree']}**")
                st.write(f"{edu['institution']}, {edu['start_year']} - {edu['end_year']}")
                st.write("---")
        
        # Experience
        with st.expander("Experience", expanded=True):
            for exp in data['experience']:
                st.write(f"**{exp['title']}**")
                st.write(f"{exp['company']}, {exp['start_date']} - {exp['end_date']}")
                st.write("Responsibilities:")
                for resp in exp['responsibilities']:
                    st.write(f"• {resp}")
                st.write("---")
        
        # Skills
        with st.expander("Skills", expanded=True):
            st.write("**Technical Skills:**")
            st.write(", ".join(data['skills']['technical']))
            st.write("\n**Soft Skills:**")
            st.write(", ".join(data['skills']['soft']))
        
        # Certifications
        if data['certifications']:
            with st.expander("Certifications", expanded=True):
                for cert in data['certifications']:
                    st.write(f"**{cert['name']}**")
                    st.write(f"{cert['issuer']}, {cert['year']}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("← Back"):
                st.session_state.form_step = 4
                st.rerun()
        with col2:
            if st.button("Edit"):
                st.session_state.form_step = 1
                st.rerun()
        with col3:
            if st.button("Generate Resume →"):
                return True
        return False
