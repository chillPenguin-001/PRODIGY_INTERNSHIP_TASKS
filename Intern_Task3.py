import re

def check_password_strength(password):
    strength_points = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # Number check
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc.).")

    # Assign strength level
    if strength_points == 5:
        strength = "Strong"
    elif strength_points >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# MAIN PROGRAM
print("=== Password Strength Checker ===")
cond = True
while cond:
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print("- " + f)
    if strength == "Strong":
        cond = False
        print("Your password is strong enough!")