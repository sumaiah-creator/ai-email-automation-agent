# 📧 AI Email Automation Agent

An Agentic AI-powered Email Automation System that reads emails from Gmail, classifies them using AI, generates summaries, creates professional replies, and allows users to send responses directly through a modern Streamlit dashboard.

---

## 🚀 Features

### 📥 Gmail Integration
- Secure Gmail OAuth Authentication
- Read emails directly from inbox
- Extract sender, subject, and body

### 🤖 AI Email Classification
Automatically categorizes emails into:
- Important
- Personal
- Meeting
- Job
- Spam

### 📝 Email Summarization
Generates concise summaries of incoming emails using AI.

### ✉️ AI Reply Generation
Creates professional and context-aware email responses automatically.

### 🧠 Agentic Workflow
The AI agent:
1. Reads emails
2. Understands content
3. Classifies intent
4. Summarizes information
5. Generates responses
6. Sends replies upon approval

### 🎨 Modern Dashboard
Built with Streamlit featuring:
- Professional dark theme
- Email management dashboard
- AI status monitoring
- Gmail connection status
- Interactive email processing

---

## 🏗️ System Architecture

```text
┌───────────────────┐
│   Gmail Inbox     │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Gmail API Reader  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  AI Email Agent   │
├───────────────────┤
│ Classification    │
│ Summarization     │
│ Reply Generation  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Streamlit UI      │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Gmail Reply Sender│
└───────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI/LLM
- Ollama
- Llama 3

### APIs
- Gmail API
- Google OAuth 2.0

### Libraries
- google-api-python-client
- google-auth-oauthlib
- requests
- pypdf

---

## 📂 Project Structure

```text
email-agent/
│
├── app.py
├── ai_agent.py
├── gmail_auth.py
├── read_emails.py
├── send_email.py
├── requirements.txt
├── credentials.json
├── token.pkl
│
├── .streamlit/
│   └── config.toml
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-email-agent.git

cd ai-email-agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download Ollama:

https://ollama.com/download

Install Llama3:

```bash
ollama run llama3
```

---

### 5. Configure Gmail API

1. Create Google Cloud Project
2. Enable Gmail API
3. Configure OAuth Consent Screen
4. Create OAuth Client ID
5. Download credentials.json
6. Place credentials.json in project root

---

### 6. Run Application

Start Ollama:

```bash
ollama run llama3
```

Open another terminal:

```bash
streamlit run app.py
```

---

## 📸 Dashboard Features

### Dashboard Overview
- AI Status Monitoring
- Gmail Connectivity Status
- Email Analytics
- Email Processing Workflow

### Email Processing
- View Email Content
- AI Categorization
- Email Summary
- AI Reply Generation
- One-Click Email Sending

---

## 🔄 Agent Workflow

```text
User Inbox
    ↓
Read Emails
    ↓
Classify Email
    ↓
Summarize Email
    ↓
Generate Reply
    ↓
Human Approval
    ↓
Send Response
```

---

## 🎯 Use Cases

- Email Management Automation
- Personal Productivity Assistant
- Customer Support Automation
- Recruitment Email Handling
- Meeting Request Management
- Smart Inbox Organization

---

## 🔒 Security Features

- OAuth 2.0 Authentication
- Secure Gmail Access
- Local Llama3 Execution
- No Third-Party Email Storage
- User Approval Before Sending Replies

---

## 📈 Future Enhancements

- Email Priority Detection
- Calendar Integration
- Attachment Analysis
- Multi-Account Support
- Email Analytics Dashboard
- Scheduled Email Responses
- Vector Database Memory
- Multi-Agent Collaboration

---

## 🎓 Learning Outcomes

Through this project:

- Built an Agentic AI System
- Integrated Large Language Models
- Implemented Gmail API
- Developed AI-powered automation workflows
- Created production-style Streamlit dashboards
- Worked with OAuth Authentication
- Designed human-in-the-loop AI systems

---

## 👨‍💻 Author

**Sumaiah**

---

## ⭐ Project Highlights

✅ Agentic AI Workflow

✅ Gmail Automation

✅ Llama3 Integration

✅ Streamlit Dashboard

✅ AI Email Classification

✅ AI Summarization

✅ Automated Reply Generation

✅ Human-in-the-Loop Decision Making
