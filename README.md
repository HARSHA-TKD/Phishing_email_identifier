🛡️ Phishing Email Identifier

Detect the warning signs. Understand the risk. Stay cyber-aware.

<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/DOMAIN-CYBERSECURITY-163A70?style=for-the-badge&logo=shield&logoColor=white" alt="Cybersecurity">
  <img src="https://img.shields.io/badge/ANALYSIS-RULE--BASED-8A9BB5?style=for-the-badge" alt="Rule based analysis">
  <img src="https://img.shields.io/badge/TESTS-UNITTEST-5B8DEF?style=for-the-badge" alt="Unit tests">
</p><p align="center">
  <strong>A Python-powered educational tool for identifying common phishing indicators in email messages.</strong>
</p>---

⚡ Project Overview

Phishing attacks use deceptive emails to trick people into clicking unsafe links, revealing sensitive information, or taking actions that compromise their security.

Phishing Email Identifier analyses user-provided email text using configurable detection rules. It identifies selected warning signs, calculates a heuristic risk score, and generates a readable report with safety recommendations.

«Built to practise Python programming, cybersecurity fundamentals, rule-based detection, and automated testing.»

🎯 Core Features

Feature| Description
🔍 Email Analysis| Inspects the sender's basic address format, subject, and body
🚨 Phrase Detection| Looks for selected urgency, sensitive-information, and reward phrases
🔗 URL Inspection| Extracts URLs and checks selected suspicious patterns
📊 Risk Assessment| Produces a heuristic score from 0 to 100
🛡️ Risk Classification| Categorises results as Low, Medium, or High
📝 Analysis Report| Displays detected indicators and safety recommendations
🧪 Automated Testing| Uses Python's built-in "unittest" framework
📋 Security Checklist| Includes a reusable manual phishing-review checklist

🧠 How It Works

       ┌─────────────────────────┐
       │   EMAIL INPUT           │
       │ Sender • Subject • Body │
       └────────────┬────────────┘
                    ▼
       ┌─────────────────────────┐
       │   TEXT ANALYSIS         │
       │ Phrase and sender rules │
       └────────────┬────────────┘
                    ▼
       ┌─────────────────────────┐
       │   URL INSPECTION        │
       │ Extract and inspect URLs│
       └────────────┬────────────┘
                    ▼
       ┌─────────────────────────┐
       │   RISK ASSESSMENT       │
       │ Score + detected clues  │
       └────────────┬────────────┘
                    ▼
       ┌─────────────────────────┐
       │   ANALYSIS REPORT       │
       │ Risk + recommendations │
       └─────────────────────────┘

📊 Risk Classification

Heuristic Score| Risk Level| Recommended Response
0–29| 🟢 Low| Remain cautious; a low score does not prove safety
30–59| 🟡 Medium| Investigate the warning signs and verify independently
60–100| 🔴 High| Treat the message as suspicious and avoid interacting with it

Important: These are project-defined scoring thresholds, not calibrated probabilities. The score indicates how many configured warning signs were detected; it does not measure the true likelihood of phishing.

🖥️ Demo Screenshots

<p align="center">
  <em>Real screenshots from the application will be displayed here.</em>
</p>Application Analysis

"Phishing Email Identifier Demo" (screenshots/phishing_detector_demo.png)

Automated Test Results

"Python Unit Test Results" (screenshots/unit_tests.png)

🛠️ Built With

Technology| Purpose
Python 3| Main programming language
"re"| Pattern matching and URL extraction
"urllib.parse"| Parsing URL components
"unittest"| Automated testing
Visual Studio Code| Development environment
Git & GitHub| Version control and project hosting

🚀 Getting Started

Prerequisites

- Python 3 installed
- Git installed (for cloning the repository)
- A terminal or Visual Studio Code

1. Clone the repository

git clone https://github.com/HARSHA-TKD/Phishing_Email_Identifier.git
cd Phishing_Email_Identifier

2. Run the application

python phishing_detector.py

On Windows, you can also use:

py phishing_detector.py

Enter a sender address, subject, and email body when prompted. Press Enter on an empty line to finish entering the body.

3. Run automated tests

python -m unittest -v

The test suite covers phrase detection, URL handling, invalid sender formats, score limits, and other input cases.

🧪 Example Analysis

Use this fictional example to demonstrate the tool:

Sender: "security@example.com"

Subject: "Urgent action required"

Body:

Your account will be closed within 24 hours.
Verify your account and password immediately.
Visit http://192.0.2.10/login

The application should identify matching configured warning signs and display a risk assessment.

"192.0.2.10" is a documentation-only example address. Do not visit the example URL.

📁 Project Structure

Phishing_Email_Identifier/
│
├── phishing_detector.py
├── test_phishing_detector.py
├── PHISHING_CHECKLIST.md
├── PROJECT_REPORT.md
├── README.md
├── .gitignore
│
└── screenshots/
    ├── phishing_detector_demo.png
    └── unit_tests.png

🔐 Privacy, Security & Limitations

- The program analyses the text supplied by the user locally.
- It does not open URLs or send email content to external services.
- Sender-format validation does not authenticate the sender.
- URL-pattern checks cannot prove that a website is malicious.
- Keyword matching can flag legitimate emails and miss sophisticated attacks.
- The tool does not perform live domain-reputation checks or machine-learning classification.
- A low-risk result does not guarantee that a message is safe.

Safety advice: Never provide passwords or OTPs in response to unexpected email requests. Verify sensitive requests through an independently obtained, trusted contact method.

📚 Project Documentation

- 📋 "Phishing Detection Checklist" (PHISHING_CHECKLIST.md)
- 📄 "Project Report" (PROJECT_REPORT.md)

🔮 Future Improvements

- Domain allowlists and configurable detection rules
- More robust email-address and URL validation
- Structured JSON report export
- Additional unit tests and test coverage reporting
- Optional integration with trusted threat-intelligence sources
- Improved handling of internationalized domains and lookalike-domain warnings

Any future URL reputation integration should be designed with privacy, safe request handling, and API-key protection in mind.

👨‍💻 Author

Harsha Vardhan V G

Cybersecurity Learner | Python Developer

Project: CodeOrbit Cybersecurity Internship — Project 3

---

<p align="center">
  <strong>Learn. Analyse. Verify. Stay Secure. 🔐</strong>
</p><p align="center">
  <sub>Educational project for cybersecurity awareness. Not a replacement for professional email-security solutions.</sub>
</p>