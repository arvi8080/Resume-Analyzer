import PyPDF2
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF resume."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.strip()


def analyze_resume_with_ai(resume_text, job_description):
    """Analyze resume using GPT model with the new OpenAI SDK."""
    prompt = f"""
    You are an expert AI career coach.
    Analyze the following resume for its suitability for this job description.

    --- RESUME ---
    {resume_text[:3000]}

    --- JOB DESCRIPTION ---
    {job_description}

    Please provide:
    1. Summary of the candidate’s profile
    2. Key strengths relevant to the role
    3. Missing skills or improvements
    4. Overall fit score (0–100)
    5. Suggestions to improve resume alignment
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # you can also use "gpt-4o" or "gpt-4-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful AI career coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
