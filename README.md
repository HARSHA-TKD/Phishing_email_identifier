🛡️ Phishing Email Identifier

<p align="center">
  <img src="https://img.shields.io/badge/Cybersecurity-Email%20Security-0A192F?style=for-the-badge&logo=protonmail&logoColor=white" alt="Cybersecurity"/>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Detection-Rule--Based-64748B?style=for-the-badge" alt="Rule-based detection"/>
  <img src="https://img.shields.io/badge/Tests-10%20Passing-16A34A?style=for-the-badge" alt="Tests"/>
</p><p align="center">
  <b>A beginner-friendly defensive security tool that analyzes suspicious email text using rule-based checks and highlights potential phishing indicators.</b>
</p>---

🎯 Overview

Phishing is a social-engineering technique in which attackers impersonate trusted organizations or individuals to trick recipients into revealing information, clicking suspicious links, or taking unsafe actions.

Phishing Email Identifier examines email text for selected warning signs and produces a simple risk assessment to help users investigate suspicious messages.

The project demonstrates how Python can be used to build a small, testable cybersecurity utility.

«Important: This is a rule-based educational detector, not a machine-learning model or a substitute for professional email-security systems.»

✨ Key Features

Feature| Description
🔎 Email text analysis| Examines supplied email text for configured warning signs
🚩 Suspicious indicators| Identifies patterns covered by the detection rules
📊 Risk assessment| Produces a result based on the implemented rules
🧪 Automated testing| Includes unit tests for expected detector behaviour
🧩 Modular Python code| Separates detection logic from test cases
📖 Security awareness| Encourages careful inspection of suspicious messages

⚙️ How It Works

        ┌──────────────────────┐
        │   Email Text Input   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Rule-Based Analysis │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Check Warning Signs  │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Display Assessment   │
        └──────────────────────┘

The detector evaluates the input using the rules implemented in the source code. Its result is an indicator for further review, not proof that an email is malicious or safe.

🧰 Tech Stack

- Language: Python 3
- Testing: Python "unittest"
- Concepts: Text analysis, conditional logic, functions, rule-based detection
- Development: Visual Studio Code / terminal
- Version control: Git and GitHub

📂 Project Structure

Phishing_email_identifier/
├── phishing_detector.py
├── test_phishing_detector.py
├── README.md
├── PHISHING_CHECKLIST.md
├── PROJECT_REPORT.md
└── screenshots/
    ├── detector-output.png
    └── test-results.png

The screenshot filenames above are examples. Keep the names in this section aligned with the files actually present in your repository.

🚀 Getting Started

1. Clone the repository

git clone https://github.com/HARSHA-TKD/Phishing_email_identifier.git
cd Phishing_email_identifier

2. Check Python

python3 --version

Python 3 is required.

3. Run the detector

python3 phishing_detector.py

Follow the prompts shown by the program, if applicable.

4. Run automated tests

python3 -m unittest -v test_phishing_detector.py

The project includes ten automated test cases for the implemented detection behaviour.

🧪 Testing

The unit tests are intended to validate the detector's behaviour on defined examples.

Coverage includes the scenarios implemented in the test suite, such as suspicious-message indicators and expected assessment results.

Run the tests locally before submitting changes. Test success demonstrates that the tested cases behave as expected; it does not establish perfect phishing detection.

🛡️ Phishing Safety Checklist

When reviewing a suspicious email:

- Verify the sender's address carefully.
- Be cautious of unexpected urgency or threats.
- Avoid opening unexpected attachments.
- Inspect links without signing in or entering personal information.
- Confirm payment requests or account alerts through official channels.
- Never share passwords or one-time verification codes in response to suspicious messages.

See ""PHISHING_CHECKLIST.md"" (PHISHING_CHECKLIST.md) for the project's checklist.

⚠️ Limitations

- Detection depends on the rules implemented in the program.
- New or cleverly disguised phishing messages may not trigger existing rules.
- Legitimate messages may contain suspicious-looking wording.
- The tool does not independently verify sender identity or website reputation unless such functionality is explicitly implemented.
- A result should not be treated as a definitive security verdict.

🔮 Future Improvements

- Add URL parsing and safer URL feature extraction.
- Support structured email files such as ".eml".
- Improve explainability by listing the triggered rules.
- Add more unit tests for edge cases.
- Explore reputation feeds or machine-learning approaches in a controlled, privacy-conscious design.

These are possible future enhancements, not claims about current functionality.

👨‍💻 Author

HARSHA VARDHAN V G

Cybersecurity Learner | Python Developer | CSE (Cybersecurity)

Program: CodeOrbit Internship — Project 3

📜 Disclaimer

This project is developed for educational and defensive-security purposes. Use it to learn about phishing awareness and rule-based text analysis. Do not use it as the sole basis for security decisions.