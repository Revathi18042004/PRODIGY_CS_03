import re

def password_strength(password):
    score = sum([
        len(password) >= 8,
        len(password) >= 12,
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[^A-Za-z0-9]', password))
    ])

    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength_levels[score]

def main():
    password = input("Enter your password: ")
    print(f"Your password strength is: {password_strength(password)}")

if __name__ == "__main__":
    main()
