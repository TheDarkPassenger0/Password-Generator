import random
import string

txt = "by TheDarkPassenger"

x = txt.title()

print(x)

# Function to generate a random password
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Start with the lowercase letters (required)
    characters = lower_case

    # Add uppercase letters if needed
    if use_uppercase:
        characters += upper_case

    # Add digits if needed
    if use_digits:
        characters += digits

    # Add special characters if needed
    if use_special_chars:
        characters += special_chars

    # Randomly choose characters for the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password


# Ask the user for password specifications
def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length and options
    length = int(input("Enter the desired length of your password (e.g., 12): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    # Display the generated password
    print("\nYour generated password is:")
    print(password)


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
