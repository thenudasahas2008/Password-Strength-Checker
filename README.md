# 🔐 Python Password Strength Checker

A beginner-friendly cybersecurity project that gives local, heuristic feedback about a password's length, character variety, and some common patterns.

## Features

- Labels a password as **Weak**, **Moderate**, or **Strong**.
- Gives feedback about length, character variety, repeated characters, and predictable sequences.
- Hides typed input in a terminal using Python's `getpass`.
- Includes automated tests using Python's built-in `unittest`.
- Uses only the Python standard library; no third-party packages are required.

## Privacy and limitations

- The program does not save or transmit the password.
- Use a made-up test password when experimenting. Do not paste your real account password into a demo tool.
- This is an educational heuristic, not a full password audit or a guarantee of security. It does not check breached-password databases and does not estimate entropy rigorously.
- Prefer long, unique passwords or passphrases and a reputable password manager. Enable multi-factor authentication when available.

## Requirements

- Python 3.9 or newer recommended.

## Run the checker

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python password_checker.py
```

On some systems, use `python3 password_checker.py` instead.

Enter a made-up test password when prompted. The characters are hidden while typing.

## Run tests

```bash
python -m unittest -v
```

The tests cover common passwords, short passwords, a long varied password, output structure, and invalid input.

## Example

```text
=== Password Strength Checker ===
Your password is checked locally and is not saved or transmitted.
Note: this basic checker is educational, not a security guarantee.

Enter a password to check:
Strength: Strong (score: 5/5)
- No obvious issues were detected by these basic checks.
- This is a simple heuristic, not a security guarantee. Prefer a unique password or passphrase and use a password manager.
```

The example output is illustrative; results depend on the test input.

## Project structure

```text
password-strength-checker/
├── password_checker.py
├── test_password_checker.py
├── README.md
├── .gitignore
└── LICENSE
```

## Learning objectives

- Practise Python functions, conditionals, regular expressions, and `getpass`.
- Understand basic password hygiene and the limitations of simplistic scoring.
- Learn unit testing and GitHub pull-request workflows.

## Suggested improvements

- Add more test cases for edge cases.
- Improve detection of common patterns without sending passwords to an online service.
- Add a documented password/passphrase guidance page.
- Review accessibility and terminal output.

## License

Released under the MIT License. See [LICENSE](LICENSE).
