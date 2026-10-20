
"""Local password strength checker.

This educational tool checks passwords locally and does not store or transmit them.
Its score is a heuristic, not a guarantee of security.
"""

from getpass import getpass
import re
import string


COMMON_PASSWORDS = {
    "123456", "123456789", "12345678", "password", "password123",
    "qwerty", "qwerty123", "111111", "admin", "letmein",
    "welcome", "iloveyou", "abc123", "000000",
}


def assess_password(password: str) -> dict:
    """Return a password assessment with a score from 0 to 100."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    feedback = []
    lowered = password.lower()

    if not password:
        return {
            "score": 0,
            "label": "Weak",
            "feedback": ["Enter a password to assess."],
        }

    if lowered in COMMON_PASSWORDS:
        return {
            "score": 0,
            "label": "Weak",
            "feedback": [
                "This is a commonly used password. Choose a unique passphrase."
            ],
        }

    length = len(password)
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    symbol = any(char in string.punctuation for char in password)
    variety_count = sum((lower, upper, digit, symbol))

    # Length contributes up to 60 points.
    score = min(length * 4, 60)

    # Character variety contributes up to 25 points.
    score += variety_count * 6
    if variety_count == 4:
        score += 1

    # Penalise predictable patterns.
    if re.search(r"(.)\1{2,}", password):
        score -= 10
        feedback.append("Avoid repeating the same character several times.")

    sequences = ("1234", "abcd", "qwerty", "password")
    if any(sequence in lowered for sequence in sequences):
        score -= 15
        feedback.append("Avoid predictable sequences and common words.")

    if length < 12:
        feedback.append("Consider using at least 12 characters.")
    if not (lower and upper):
        feedback.append("Consider mixing uppercase and lowercase letters.")
    if not digit:
        feedback.append("Consider including numbers.")
    if not symbol:
        feedback.append("Consider including symbols where appropriate.")

    score = max(0, min(score, 100))

    if length >= 16 and score >= 75:
        label = "Strong"
    elif length >= 12 and score >= 45:
        label = "Moderate"
    else:
        label = "Weak"

    if not feedback:
        feedback.append("No obvious issues were detected by these basic checks.")

    feedback.append(
        "This heuristic is not a security guarantee. Use a unique passphrase "
        "and a password manager."
    )

    return {"score": score, "label": label, "feedback": feedback}


def main() -> None:
    print("=== Password Strength Checker ===")
    print("Your password is checked locally and is not saved or transmitted.")

    password = getpass("Enter a password to check: ")
    if not password:
        print("No password entered.")
        return

    result = assess_password(password)
    print(f"\nStrength: {result['label']} (score: {result['score']}/100)")
    for item in result["feedback"]:
        print(f"- {item}")


if __name__ == "__main__":
    main()
