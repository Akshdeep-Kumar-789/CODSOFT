import random
import string

def genpass(length, complexity):
    char_pools = [
        string.ascii_lowercase,                          # Complexity 1
        string.ascii_lowercase + string.ascii_uppercase, # Complexity 2
        string.ascii_letters + string.digits,            # Complexity 3
        string.ascii_letters + string.digits + string.punctuation  # Complexity 4
    ]
    if complexity < 1 or complexity > 4:
        complexity = 4 # Default
    characters = char_pools[complexity - 1]
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Invalid length. Please enter a positive number.")
            return
        complexity = int(input("Enter the desired complexity (1-4):\n1. Lowercase\n2. Lowercase + Uppercase\n3. Lowercase + Uppercase + Digits\n4. Lowercase + Uppercase + Digits + Special Chars\nYour choice: "))
        if complexity < 1 or complexity > 4:
            print("Invalid complexity level. Using maximum complexity.")
            complexity = 4
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    password = genpass(length, complexity)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()