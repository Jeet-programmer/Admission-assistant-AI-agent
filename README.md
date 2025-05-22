# 🎓 Admission Assistant AI Agent

A conversational AI agent built to assist students with **college admission-related queries** — from scholarships and tuition fees to student loans and eligibility criteria. This intelligent assistant leverages natural language understanding and a user-friendly Streamlit interface to provide accurate and instant responses to admission inquiries.

> 🔗 [GitHub Repo](https://github.com/Jeet-programmer/Admission-assistant-AI-agent.git)

---

## 🧠 Project Overview

The **Admission Assistant AI Agent** is designed to automate and streamline the admission support process for universities and colleges. It reduces the burden on helpdesks by instantly answering student queries related to:

* 🎓 **Admission Process**
* 💸 **Scholarships & Financial Aid**
* 🏦 **Student Loans**
* 📋 **Eligibility Criteria**
* 📅 **Important Dates**
* 💰 **Tuition & Fee Structure**

The AI agent uses a backend powered by a language model and is deployed via a Streamlit web UI for easy access.

---

## 📁 Repository Structure

```
Admission-assistant-AI-agent/
├── main.py                  # Core logic of the AI agent
├── requirements.txt         # Python dependencies
├── admission_details.pdf    # Reference document with all admission-related info
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Jeet-programmer/Admission-assistant-AI-agent.git
cd Admission-assistant-AI-agent
```

### 2. Set Up Environment

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

To launch the assistant in your browser:

```bash
streamlit run main.py
```

---

## 📘 Reference Data

The agent relies on `admission_details.pdf`, which contains detailed information about:

* Scholarships offered
* Tuition fee breakdown
* Loan assistance and documentation
* Admission timelines and deadlines

The PDF is either parsed or used as a knowledge base to answer incoming queries.

---

## 🧩 How It Works

* `main.py`: Contains the logic for handling queries, extracting answers, and processing the knowledge base.
---

## 🛠 Tech Stack

* **Python 3.10+**
* **Streamlit** – for building the interactive UI
* **LangChain / LLMs** (if used) – for semantic query handling
* **PyPDF2 / pdfminer** – for reading admission details
* **FAISS / VectorDB** (optional) – for embedding-based retrieval

---

## 💡 Use Cases

* University admission helpdesk automation
* College inquiry bots
* Educational consultancy tools
* Chatbot for institutional websites

---

## 📃 License

MIT License © 2025 [Jeet-programmer](https://github.com/Jeet-programmer)

---

## 🙋‍♂️ Contributing

Feel free to fork this repo and submit PRs if you'd like to contribute features such as:

* Multi-language support
* FAQ integration
* WhatsApp or Telegram deployment
* Admin dashboard for query analytics
