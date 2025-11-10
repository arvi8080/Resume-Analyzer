import streamlit as st
from utils import extract_text_from_pdf, analyze_resume_with_ai

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🤖", layout="centered")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and job description to get instant AI feedback!")

uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("🧾 Paste Job Description Here", height=200)

if st.button("🔍 Analyze Resume"):
    if uploaded_file is not None and job_description.strip():
        with st.spinner("Analyzing resume... please wait ⏳"):
            try:
                resume_text = extract_text_from_pdf(uploaded_file)
                ai_feedback = analyze_resume_with_ai(resume_text, job_description)
                st.success("✅ Analysis Complete!")
                st.markdown("### 🧠 AI Feedback:")
                st.write(ai_feedback)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please upload a resume and paste a job description.")
