def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(not char.isalnum() for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("\nPassword strength:", strength)
    if feedback:
        print("Suggestions:")
        for item in feedback:
            print("-", item)


print("=== Password Strength Checker ===")
user_password = input("Enter a password to check: ")
check_password(user_password)