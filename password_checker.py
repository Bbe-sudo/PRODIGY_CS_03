import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count how many criteria are met
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Feedback messages
    feedback = []
    if length_error:
        feedback.append("❌ Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append("❌ Add at least one uppercase letter.")
    if lowercase_error:
        feedback.append("❌ Add at least one lowercase letter.")
    if digit_error:
        feedback.append("❌ Include at least one number.")
    if special_char_error:
        feedback.append("❌ Include at least one special character (!, @, #, $, etc.)")

    # Strength level
    if score == 5:
        strength = "💪 Very Strong"
    elif score == 4:
        strength = "🔒 Strong"
    elif score == 3:
        strength = "⚠️ Medium"
    else:
        strength = "❗ Weak"

    print("\nPassword Strength:", strength)
    if feedback:
        print("Feedback:")
        for msg in feedback:
            print("-", msg)

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
