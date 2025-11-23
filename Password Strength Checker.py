import re
import time
from pyfiglet import Figlet
from termcolor import colored

def estimate_crack_time(password):
    """
    Estimate password strength based on length and character variety.
    Returns a professional, neutral description of time to brute-force.
    """
    length = len(password)
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_num = re.search(r'[0-9]', password)
    has_special = re.search(r'[^a-zA-Z0-9]', password)

    if length < 8:
        return "Very short (highly vulnerable)"
    elif length >= 12 and (has_lower and has_upper and has_num and has_special):
        return "Extremely strong (very resistant)"
    elif length >= 10 and (has_lower and has_upper and has_num):
        return "Moderately strong"
    else:
        return "Weak"

def check_strength(password):
    """
    Check password strength and return structured feedback.
    """
    feedback = []
    length = len(password)

    if length < 8:
        feedback.append(colored("Length: Less than 8 characters (Weak)", "red"))
    else:
        feedback.append(colored(f"Length: {length} characters", "green"))

    # Check for character types
    checks = {
        "Lowercase letters": re.search(r'[a-z]', password),
        "Uppercase letters": re.search(r'[A-Z]', password),
        "Numbers": re.search(r'[0-9]', password),
        "Special characters": re.search(r'[^a-zA-Z0-9]', password)
    }

    for name, check in checks.items():
        if check:
            feedback.append(colored(f"{name}: Present", "green"))
        else:
            feedback.append(colored(f"{name}: Missing", "yellow"))

    return feedback

def main():
    """
    Main program loop: prompts for passwords and displays professional analysis.
    """
    f = Figlet(font='slant')
    print(colored(f.renderText('PASSWORD CHECKER 9000'), 'cyan'))
    print("\n" + "="*50)
    print("This tool analyzes password strength based on character composition and length.")
    print("="*50 + "\n")

    while True:
        password = input("Enter a password to test (or type 'quit'): ").strip()

        if password.lower() == 'quit':
            print("\n" + "="*50)
            print(colored("Thank you for using Password Checker 9000", "magenta"))
            print("="*50 + "\n")
            break

        if not password:
            print(colored("Input cannot be empty. Please enter a valid password.", "red"))
            continue

        print("\nAnalyzing password...\n")
        time.sleep(0.5)

        feedback = check_strength(password)
        crack_time = estimate_crack_time(password)

        print("RESULTS:")
        print("\n".join(feedback))
        print(colored(f"\nEstimated resistance to brute-force attack: {crack_time}", "magenta"))
        print("-"*50 + "\n")

if __name__ == "__main__":
    main()
