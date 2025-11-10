👇

🤖 AI Resume Analyzer
AI Resume Analyzer is an intelligent tool built with Streamlit and OpenAI GPT that helps job seekers optimize their resumes for specific roles.
Just upload your resume (PDF) and paste a job description — the AI instantly gives you detailed feedback, highlights skill gaps, and provides improvement suggestions.

🚀 Features
✅ Upload your resume (PDF format)
✅ Paste a job description for your desired role
✅ Get AI-powered feedback on:


Resume-job match percentage


Missing keywords and skills


Actionable improvement tips
✅ Clean and interactive Streamlit web interface
✅ Works locally or can be deployed on the web (Streamlit Cloud / Render)



🧠 Tech Stack


Python 3.10+


Streamlit – for web UI


OpenAI GPT API – for AI feedback


PyPDF2 – for extracting text from resumes


dotenv – for managing API keys



🗂️ Project Structure
AI-Resume-Analyzer/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # All dependencies
├── .env                  # OpenAI API Key (not uploaded to GitHub)
├── README.md             # Project documentation
└── sample_resume.pdf     # Example resume file (optional)


⚙️ Installation and Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key
Create a .env file in the root directory:
OPENAI_API_KEY=your_api_key_here

5️⃣ Run the App
streamlit run app.py

Then open your browser and go to 👉 https://resume-analyzer-nwrzr3y8xw8v5ejkuyszhk.streamlit.app/

🌍 Deployment (Streamlit Cloud)


Push your project to GitHub


Go to Streamlit Cloud


Click "New app"


Connect your GitHub repo and select the branch & app.py


In Secrets, add:
OPENAI_API_KEY=your_api_key_here



Click Deploy — your app will go live! 🎉



🧩 Example Output
Input:


Resume: My_resume.pdf


Job Description: “AI Engineer with skills in Python, ML, NLP”


Output:
✅ Resume Match Score: 82%
🧠 Missing Skills: TensorFlow, MLOps, LLM Fine-tuning
💡 Suggestions:
- Add a project demonstrating NLP experience.
- Emphasize hands-on model deployment experience.


🧑‍💻 Author
Arvind Prajapati
💼 AI & Web Developer | 🚀 Passionate about building AI-powered tools
🔗 LinkedIn
💻 GitHub

⭐ Show Your Support
If you like this project, please give it a ⭐ on GitHub — it helps others find it too!

