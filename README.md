# SmartAction - Email Summarizer

SmartAction is a lightweight AI-powered app that automatically summarizes emails into short, clear, and actionable summaries.  
It was created as a personal project to explore Natural Language Processing (NLP) and text summarization using Hugging Face models.

---

## Project Overview

SmartAction leverages transformer models to generate concise summaries of long emails while preserving the main context and tone.  
The app also includes automatic language detection, allowing it to process both English and French emails seamlessly.

Its main goal is to save time and improve productivity when reading lengthy messages.

---

## How It Works

1. Upload a `.txt` file containing your email content.  
2. The app automatically detects the language (English or French).  
3. It uses a summarization model to generate a clear, short version of the email.  
4. The summary is displayed instantly in the interface.

---

## Technologies Used

| Purpose | Library |
|----------|----------|
| Web Interface | Streamlit |
| Summarization Model | Transformers (Hugging Face) |
| Language Detection | LangDetect |
| Python Version | 3.11 |

---

## Installation and Execution

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/SmartAction.git
cd SmartAction

# Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# Install dependencies and launch the app
pip install -r requirements.txt
streamlit run app.py
