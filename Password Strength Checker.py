import re  
import time 
from pyfiglet import Figlet 
from termcolor import colored  

def estimate_crack_time(password):

    length = len(password)
    has_lower = re.search(r'[a-z]', password)  
    has_upper = re.search(r'[A-Z]', password) 
    has_num = re.search(r'[0-9]', password)  
    has_special = re.search(r'[^a-zA-Z0-9]', password) 
    
    if length < 8:
        return "Instant (Weak af)"
    elif length >= 12 and (has_lower and has_upper and has_num and has_special):
        return "Like a million years (Good job!)"
    elif length >= 10 and (has_lower and has_upper and has_num):
        return "Few years (Not bad)"
    else:
        return "Few days (My grandma could crack this)"

def check_strength(password):
    feedback = []  # this will store all the messages
    length = len(password)
    
    if length < 8:
        feedback.append(colored("❌ Too short (hackers love short passwords)", "red"))
    else:
        feedback.append(colored(f"✅ Length: {length} chars (decent)", "green"))
    
    # Checking for different character types
    checks = {
        "Lowercase letters": re.search(r'[a-z]', password),
        "Uppercase letters": re.search(r'[A-Z]', password),
        "Numbers": re.search(r'[0-9]', password),
        "Special chars": re.search(r'[^a-zA-Z0-9]', password) 
    }
    
    # Add check results to feedback
    for name, check in checks.items():
        if check:
            feedback.append(colored(f"✅ Has {name}", "green"))
        else:
            feedback.append(colored(f"❌ Missing {name}", "yellow"))
    
    return feedback

def main():
    f = Figlet(font='slant')
    print(colored(f.renderText('PASSWORD CHECKER 9000'), 'cyan'))
    print(colored("(Now with 100% more security!)", "yellow"))
    print("\n" + "="*50)
    print("Warning: This isn't real security advice")
    print("I just learned Python last month")
    print("="*50 + "\n")
    
    # Keep running until user quits
    while True:
        password = input("\nTest a password (or type 'quit'): ").strip()
        
        # Exit if user types quit
        if password.lower() == 'quit':
            print("\n" + "="*50)
            print(colored("Thanks for using my janky program!", "magenta"))
            print("Follow me on GitHub @YourUsernameHere")
            print("="*50 + "\n")
            break
        
        print("\n" + "-"*40)
        print(colored("\nAnalyzing password...", "blue"))
        time.sleep(1.5) 
        print(colored("Asking my hacker friends...", "blue"))
        time.sleep(0.5)
        print(colored("Calculating...", "blue"))
        time.sleep(0.3)
        

        feedback = check_strength(password)
        crack_time = estimate_crack_time(password)
        
        # Show results
        print("\nRESULTS:")
        print("\n".join(feedback))
        print(colored(f"\n⏳ Time to crack: {crack_time}", "magenta"))
        print("-"*40 + "\n")

if __name__ == "__main__":
    main()
