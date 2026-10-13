"""Automated tests for the Phishing Email Identifier."""

import unittest

from phishing_detector import (
    analyze_email,
    analyze_url,
    extract_urls,
)


class TestPhishingDetector(unittest.TestCase):

    def test_urgent_language_is_detected(self):
        result = analyze_email(
            "security@example.com",
            "Urgent action required",
            "Your account will be closed. Act now.",
        )
        self.assertGreater(result["score"], 0)
        self.assertTrue(result["findings"])

    def test_sensitive_information_is_detected(self):
        result = analyze_email(
            "support@example.com",
            "Account verification",
            "Please provide your password and OTP.",
        )
        self.assertTrue(
            any(
                finding["category"] == "Sensitive-information request"
                for finding in result["findings"]
            )
        )

    def test_ip_address_url_warning(self):
        findings = analyze_url("http://192.0.2.10/login")
        self.assertTrue(
            any("IP address" in warning for warning in findings)
        )

    def test_url_extraction(self):
        urls = extract_urls(
            "Visit https://example.com/help for information."
        )
        self.assertIn("https://example.com/help", urls)

    def test_normal_email_has_low_score(self):
        result = analyze_email(
            "help@example.com",
            "Hello",
            "Just a friendly greeting.",
        )
        self.assertEqual(result["risk"], "LOW")
        self.assertEqual(result["score"], 0)

    def test_score_never_exceeds_100(self):
        result = analyze_email(
            "security@example.com",
            "Urgent action required",
            (
                "Act now. Verify your account and password. "
                "Your account will be closed. "
                "http://192.0.2.10/login"
            ),
        )
        self.assertLessEqual(result["score"], 100)

    def test_duplicate_urls_are_analyzed_once(self):
        result = analyze_email(
            "security@example.com",
            "Please review",
            (
                "Visit http://192.0.2.10/login "
                "or http://192.0.2.10/login"
            ),
        )
        self.assertEqual(len(result["urls_found"]), 1)

    def test_invalid_sender_is_flagged(self):
        result = analyze_email(
            "not-a-valid-address",
            "Hello",
            "Please review this message.",
        )
        self.assertTrue(
            any(
                finding["category"] == "Sender"
                for finding in result["findings"]
            )
        )

    def test_empty_message_does_not_crash(self):
        result = analyze_email("", "", "")
        self.assertIsInstance(result["score"], int)
        self.assertIn(result["risk"], ["LOW", "MEDIUM", "HIGH"])

    def test_https_url_is_not_flagged_for_http(self):
        findings = analyze_url("https://example.com/help")
        self.assertFalse(
            any("unencrypted HTTP" in warning for warning in findings)
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)