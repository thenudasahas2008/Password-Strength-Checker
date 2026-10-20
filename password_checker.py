"""Local password strength checker.

The password is entered with getpass so it is not echoed in the terminal.
This tool does not store or transmit passwords. Its score is a heuristic,
not a guarantee that a password is secure.
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
    """Return a heuristic assessment without storing the supplied password."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    length = len(password)
    lower = any(char.islower() for char in password)
    upper = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    symbol = any(char in string.punctuation for char in password)
    variety_count = sum((lower, upper, digit, symbol))

    feedback = []
    score = 0

    if password.lower() in COMMON_PASSWORDS:
        return {
            "score": 0,
            "label": "Weak",
            "feedback": [
                "This is a commonly used password. Choose a unique passphrase instead."
            ],
        }

    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Use at least 12 characters; longer is generally better.")

    if variety_count >= 3:
        score += 2
    elif variety_count == 2:
        score += 1
    else:
        feedback.append(
            "Consider using a mix of uppercase/lowercase letters, numbers, "
            "and symbols where appropriate."
        )

    lowered = password.lower()
    if re.search(r"(.)\1{2,}", password):
        score -= 1
        feedback.append("Avoid repeating the same character several times.")

    common_sequences = ("1234", "abcd", "qwerty", "password")
    if any(sequence in lowered for sequence in common_sequences):
        score -= 1
        feedback.append("Avoid predictable sequences and common words.")

    if length >= 16 and variety_count >= 3 and score >= 4:
        label = "Strong"
    elif length >= 12 and score >= 2:
        label = "Moderate"
    else:
        label = "Weak"

    if not feedback:
        feedback.append("No obvious issues were detected by these basic checks.")
    feedback.append(
        "This is a simple heuristic, not a security guarantee. Prefer a unique "
        "password or passphrase and use a password manager."
    )

    return {"score": max(score, 0), "label": label, "feedback": feedback}


def main() -> None:
    print("=== Password Strength Checker ===")
    print("Your password is checked locally and is not saved or transmitted.")
    print("Note: this basic checker is educational, not a security guarantee.\n")

    password = getpass("Enter a password to check: ")
    if not password:
        print("No password entered.")
        return

    result = assess_password(password)
    print(f"\nStrength: {result['label']} (score: {result['score']}/5)")
    for item in result["feedback"]:
        print(f"- {item}")


if __name__ == "__main__":
    main()
