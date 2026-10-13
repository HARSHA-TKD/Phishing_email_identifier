# Project Report: Phishing Email Identifier

## 1. Introduction
Phishing is a social-engineering technique in which attackers
use deceptive messages to persuade people to reveal sensitive
information, click unsafe links, or perform unwanted actions.

This project demonstrates a Python-based, rule-driven approach
to identifying selected warning signs in email messages.

## 2. Objectives
- Identify common phishing indicators in email text.
- Inspect URLs for selected suspicious patterns.
- Generate a heuristic risk score and readable report.
- Practise Python programming and automated testing.
- Promote safer email-handling practices.

## 3. Technologies Used
- Python 3
- Regular expressions
- Python urllib.parse module
- Python unittest framework
- Visual Studio Code
- Git and GitHub

## 4. System Design
The program accepts a sender address, subject, and email body.
It checks configured phrases, validates the basic sender format,
extracts URLs, and examines selected URL characteristics.

The detected indicators contribute to a capped heuristic score.
The program then displays a risk category, findings, and a
recommendation.

## 5. Risk Classification
- Low: score below 30
- Medium: score from 30 through 59
- High: score of 60 or above

These thresholds are demonstration rules, not calibrated
probabilities of phishing.

## 6. Testing
Automated unit tests cover:
- Urgent wording detection
- Sensitive-information keyword detection
- URL warning detection
- URL extraction
- Normal-message handling
- Score limit
- Duplicate URL handling
- Invalid sender format
- Empty input
- HTTPS URL handling

Record the actual test results before submitting this report.

## 7. Limitations
- Keyword rules may flag legitimate emails.
- Sophisticated phishing emails may evade detection.
- Sender-format validation does not authenticate a sender.
- URL patterns alone cannot establish whether a site is malicious.
- The tool does not perform reputation checks or machine learning.
- A low score does not prove an email is safe.

## 8. Ethical and Safety Considerations
The tool analyses user-provided text locally and does not open
URLs or transmit email content. Fictional sample emails should
be used for demonstrations.

## 9. Conclusion
The project demonstrates how Python can support basic
phishing-awareness training through rule-based analysis,
structured reporting, and automated testing.

The tool is intended for education and should not replace
security software or independent verification.

## 10. Author and Submission Details
Author: Harsha Vardhan V G
Project: CodeOrbit Internship — Project 3
Language: Python