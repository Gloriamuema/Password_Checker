import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Strength evaluation
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = 5 - sum(errors)

    if strength == 5:
        return "✅ Strong Password"
    elif 3 <= strength < 5:
        return "⚠️ Medium Strength Password"
    else:
        return "❌ Weak Password"

# --- Main Program ---
password = input("Enter a password to check: ")
print(check_password_strength(password))
# Password Strength Checker
# This program checks the strength of a given password based on length and character variety.
# Criteria:
# - At least 8 characters long
# - Contains at least one digit
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one special character (e.g., !@#$%^&*)
# The program evaluates the password and provides feedback on its strength.
# Example Usage:
# Enter a password to check: P@ssw0rd
# ✅ Strong Password
# Enter a password to check: password
# ❌ Weak Password
# Enter a password to check: Pass123
# ⚠️ Medium Strength Password
