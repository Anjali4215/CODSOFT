import random
import string

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

def generate_password(length, choices):
    char_sets = []
    if 1 in choices:
        char_sets.append(string.ascii_uppercase)
    if 2 in choices:
        char_sets.append(string.ascii_lowercase)
    if 3 in choices:
        char_sets.append(string.digits)
    if 4 in choices:
        char_sets.append(special_chars)
    
    if not char_sets:
        return "No character type selected!"
    
    # Ensure at least one character from each selected type
    password = [random.choice(cs) for cs in char_sets]
    
    # Fill the remaining length
    all_chars = ''.join(char_sets)
    password += [random.choice(all_chars) for _ in range(length - len(password))]
    
    random.shuffle(password)
    return ''.join(password)

# ===== Main Program =====
while True:
    print("\nPassword Generator Options:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Digits")
    print("4. Special symbols")
    print("You can select multiple options by separating numbers with commas (e.g., 1,3,4)")

    try:
        selected = input("Enter your choice(s): ")
        choices = [int(x.strip()) for x in selected.split(",")]
        if any(c not in [1,2,3,4] for c in choices):
            print("Invalid choice(s). Please select numbers 1-4 only.")
            continue

        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be positive.")
            continue

       
        password = generate_password(length, choices)
        print("Generated Password:", password)

        another = input("Generate another password with same options? (y/n): ").strip().lower()
        if another != "y":
            break

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    restart = input("Do you want to start over and choose options again? (y/n): ").strip().lower()
    if restart != "y":
        print("Exiting password generator. Goodbye!")
        break
