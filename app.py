import streamlit as st
from docx import Document
import google.generativeai as genai
import os

# =================== CONFIGURATION ===================
API_KEY = "AIzaSyDdIeXyFARghqqbschVIPGamF3akDHfDT4"  # <-- Replace with your Gemini API Key
genai.configure(api_key=API_KEY)


# =================== HELPER FUNCTIONS ===================

def convert_docx_to_text(uploaded_file):

    """Converts a .docx file to plain text."""
    try:
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        st.error(f"❌ Error reading the .docx file: {e}")
        return None

def analyze_resume_with_gemini(resume_text):
    """Analyzes resume text using Gemini API."""
    prompt = f"""
You are a professional resume reviewer.

Please analyze the following resume and provide:

1. **Pros** - strong skills, technologies, achievements, or experiences.
2. **Cons** - missing skills, vague areas, weak points, or areas for improvement.

Return your answer in the following format:

Pros:
- ...

Cons:
- ...

Resume:
\"\"\"
{resume_text}
\"\"\"
    """
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error calling Gemini API: {e}"


# =================== STREAMLIT UI ===================

st.set_page_config(page_title="Resume Analyzer with Gemini", page_icon="🧠")
st.title("📄 Resume Analyzer using Google Gemini AI")
st.markdown("Upload your **.docx resume** and get **Pros and Cons** analysis.")

uploaded_file = st.file_uploader("Upload your resume (.docx)", type=["docx"])

if uploaded_file:
    with st.spinner("🔄 Reading and analyzing your resume..."):
        resume_text = convert_docx_to_text(uploaded_file)

        if resume_text:
            analysis_result = analyze_resume_with_gemini(resume_text)
            st.success("✅ Analysis complete!")

            st.markdown("### 📈 Gemini Resume Analysis")
            st.markdown("```\n" + analysis_result + "\n```")
else:
    st.info("📤 Please upload a .docx resume file to get started.")
