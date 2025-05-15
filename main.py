

import streamlit as st
import requests
import json
import fitz  # PyMuPDF
from dotenv import load_dotenv
import os
load_dotenv()

# === Configuration ===
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
PDF_PATH = "Academic Eligibility Criteria.pdf"


# === PDF Extraction ===
def extract_pdf_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

# === Ask Gemini with PDF context ===
def ask_gemini_with_pdf_context(user_query):
    try:
        pdf_text = extract_pdf_text(PDF_PATH)

        prompt = (
            "Using the following academic eligibility criteria document, "
            "answer the user's question.\n\n"
            f"=== Academic Eligibility Criteria ===\n{pdf_text}\n\n"
            f"=== User's Question ===\n{user_query}"
        )

        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Gemini API error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Error communicating with Gemini API: {e}"

# === Agents ===
class DocumentCheckerAgent:
    def check_documents(self, application):
        required_docs = ["id_proof", "transcript", "photo"]
        missing = [doc for doc in required_docs if not application.get(doc)]
        if missing:
            return False, f"Missing documents: {', '.join(missing)}"
        return True, "All documents are valid"

class ShortlistingAgent:
    def shortlist(self, application):
        if application.get("grade", 0) >= 75:
            return True, "Candidate shortlisted"
        return False, "Candidate not eligible"

class StudentCounsellorAgent:
    def communicate(self, student_name):
        return f"Email sent to {student_name} with admission updates."

class StudentLoanAgent:
    def process_loan(self, amount):
        if amount <= 50000:
            return True, "Loan approved"
        return False, "Loan amount exceeds limit"

# === Streamlit App ===
def run_app():
    st.title("🎓 Automated Admission Helpdesk")

    st.sidebar.header("Student Application Input")
    student_name = st.sidebar.text_input("Student Name")
    grade = st.sidebar.number_input("Grade (%)", min_value=0, max_value=100)
    id_proof = st.sidebar.checkbox("ID Proof Submitted")
    transcript = st.sidebar.checkbox("Transcript Submitted")
    photo = st.sidebar.checkbox("Photo Submitted")
    loan_requested = st.sidebar.checkbox("Apply for Student Loan?")
    loan_amount = st.sidebar.number_input("Loan Amount", min_value=0)

    if st.sidebar.button("Submit Application"):
        st.subheader("📄 Document Check")
        docs = {
            "id_proof": id_proof,
            "transcript": transcript,
            "photo": photo
        }
        doc_agent = DocumentCheckerAgent()
        doc_result, doc_msg = doc_agent.check_documents(docs)
        st.write(doc_msg)

        if doc_result:
            st.subheader("📌 Shortlisting")
            shortlister = ShortlistingAgent()
            shortlist_result, shortlist_msg = shortlister.shortlist({"grade": grade})
            st.write(shortlist_msg)

            if shortlist_result:
                st.subheader("📬 Student Communication")
                counsellor = StudentCounsellorAgent()
                comm_msg = counsellor.communicate(student_name)
                st.write(comm_msg)

                if loan_requested:
                    st.subheader("💰 Loan Processing")
                    loan_agent = StudentLoanAgent()
                    loan_result, loan_msg = loan_agent.process_loan(loan_amount)
                    st.write(loan_msg)

    st.subheader("🤖 Director's Assistant (Gemini with PDF Context)")
    query = st.text_input("Ask Gemini about the admission process:")
    if st.button("Ask Gemini"):
        with st.spinner("Thinking..."):
            response = ask_gemini_with_pdf_context(query)
            st.write(response)

# Run
if __name__ == "__main__":
    run_app()


