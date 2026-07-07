# 🛡️ Phishing Detection and Automated Mitigation System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Cybersecurity-Phishing%20Detection-success?style=for-the-badge" />
</p>

<p align="center">
An AI-powered phishing detection system that scans Gmail inboxes, calculates phishing risk scores using a custom Risk Engine, classifies emails into <b>Safe</b>, <b>Suspicious</b>, or <b>Phishing</b>, and automatically mitigates phishing attacks by moving malicious emails to the Spam folder.
</p>

---

# 📖 Overview

Phishing emails remain one of the leading causes of cyberattacks. This project automates the process of detecting phishing emails by continuously scanning a user's Gmail inbox and analyzing every incoming email using a custom-built **Risk Engine**.

Instead of relying on a single feature, the Risk Engine evaluates multiple characteristics of an email—including sender authenticity, hyperlinks, subject line, content, and header information—to generate a phishing risk score.

Based on this score, emails are classified into:

- ✅ Safe
- ⚠️ Suspicious
- 🚨 Phishing

Whenever an email is classified as **Phishing**, the application:

- Generates an instant security alert.
- Automatically moves the email to the Spam folder.
- Stores phishing information for future analysis.

---

# ✨ Features

- Gmail inbox scanning
- AI-based phishing detection
- Custom Risk Engine for phishing score calculation
- Safe / Suspicious / Phishing classification
- Automatic phishing alerts
- Automatic movement of phishing emails to Spam
- REST APIs using FastAPI
- MySQL database integration
- Secure authentication
- Optimized phishing record management

---

# 🧠 Hybrid AI Risk Engine

The core of the system is a **Hybrid AI Risk Engine** that combines the semantic understanding of a Transformer model with custom phishing detection heuristics to accurately assess email threats.

Rather than relying solely on a machine learning prediction, the Risk Engine evaluates multiple security signals and computes a final phishing risk score.

### AI-Based Analysis

A pre-trained **Hugging Face Transformer model** analyzes the semantic meaning of the email to identify phishing intent that traditional keyword-based filters may miss.

### Custom Risk Scoring

The Transformer prediction is combined with a custom scoring mechanism built specifically for phishing detection.

The engine evaluates features such as:

- Sender authenticity
- Sender domain analysis
- Suspicious URLs
- Email subject
- Email body content
- Header anomalies
- Hyperlink characteristics
- AI confidence score

Each feature contributes a weighted score, producing a final **Risk Score** between **0–100**.


This hybrid approach improves detection by combining contextual understanding from Transformer models with cybersecurity-specific heuristics, reducing false positives while maintaining high phishing detection accuracy.

---

# ⚙️ System Workflow

```text
User Login
      │
      ▼
Connect to Gmail Inbox
      │
      ▼
Fetch Incoming Emails
      │
      ▼
Extract Email Features
      │
      ▼
Risk Engine Analysis
      │
      ▼
Generate Phishing Risk Score
      │
      ▼
Classify Email
 ┌────────────┬────────────┬
 │            │            │
 ▼            ▼            ▼
Safe     Suspicious    Phishing
                           │
                           ▼
                 Generate Alert
                           │
                           ▼
            Move Email to Spam Folder
                           │
                           ▼
                  Store Scan Results
```

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy

### Database
- PostgreSQL

### AI / Machine Learning
- Hugging Face Transformers
- Scikit-learn
- Custom Hybrid Risk Engine

## APIs

- REST API

## Authentication

- JWT Authentication

## Email Service

- Gmail API / IMAP

## Version Control

- Git
- GitHub

---

## 📂 Project Structure

```text
Phishing-Detection-and-Automated-Mitigation/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   ├── assets/
│   └── public/
│
├── backend/
│   ├── api.py                 # FastAPI API routes
│   ├── gmail_reader.py        # Gmail inbox scanner
│   ├── database.py            # PostgreSQL configuration
│   ├── models.py              # Database models
│   └── auth.py                # Authentication services
│
├── risk_engine/
│   ├── phishing_model.py      # Transformer-based phishing classifier
│   ├── risk_engine.py         # Hybrid AI risk scoring logic
│   ├── feature_extractor.py   # Email feature extraction
│   └── test_detection.py      # Testing and evaluation
│
├── database/
│   ├── schema.sql
│   └── migrations/
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .env
```
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/phishing-detection.git

cd phishing-detection
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
DATABASE_URL=mysql://username:password@localhost/database
SECRET_KEY=your_secret_key
```

---

## Run the Application

```bash
uvicorn api:app --reload
```

Server starts on:

```
http://127.0.0.1:8000
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|----------|-----------|-------------|
| POST | `/login` | User Login |
| POST | `/signup` | Register User |
| GET | `/scan` | Scan Gmail Inbox |
| GET | `/notifications` | View Alerts |
| GET | `/history` | Scan History |
| GET | `/dashboard` | Dashboard Data |

---

# 📸 Screenshots

Added screenshots of the application inside a `screenshots` folder.

Example:

```text
screenshots/
│
├── login.png
├── dashboard.png
├── inbox.png
├── risk-engine.png
├── notifications.png
└── phishing-result.png
```

---

# 🎯 Future Improvements

- Deep Learning based phishing detection
- Real-time email monitoring
- URL reputation integration
- Attachment malware scanning
- Browser Extension
- Explainable AI for phishing predictions
- Multi-account email support
- Admin dashboard with analytics

---

# 👨‍💻 Contributors

**Dipti Shaw**,
**Ayushi Kumari** and
**Harshita Gupta**
B.Tech Computer Science & Engineering

GitHub: https://github.com/Dipti-shaw

---

# 📄 License

This project is developed for educational and research purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It motivates further development and helps others discover the project.
