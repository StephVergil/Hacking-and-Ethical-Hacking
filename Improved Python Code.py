from zxcvbn import zxcvbn
import getpass
import sys
import math

def calculate_entropy(password):
    """Estimate the entropy (complexity) of a given password."""
    if len(password) == 0:
        return 0  # No password, so no entropy
    charset = 0  # Start with an empty character set
    if any(c.islower() for c in password): charset += 26  # Add lowercase letters
    if any(c.isupper() for c in password): charset += 26  # Add uppercase letters
    if any(c.isdigit() for c in password): charset += 10  # Add digits
    if any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for c in password): charset += 32  # Add special characters
    # Calculate entropy by multiplying password length by log base 2 of charset size
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def test_single_password(output_file=None):
    """Check the strength of one password."""
    password = getpass.getpass("[?] Enter your password: ")  # Securely input password
    result = zxcvbn(password)  # Get the password strength analysis
    entropy = calculate_entropy(password)  # Calculate the entropy

    # Prepare output to show
    output = (
        f"Value: {result['password']}\n"
        f"Password Score: {result['score']}/4\n"
        f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}\n"
        f"Entropy (bits): {entropy:.2f}\n"
        f"Feedback: {', '.join(result['feedback']['suggestions']) if result['feedback']['suggestions'] else 'None'}\n"
    )
    print(output)  # Display the results

    # If an output file is provided, save the result to that file
    if output_file:
        with open(output_file, 'a') as file:
            file.write(output + '\n')

def test_multiple_passwords(password_file, output_file=None):
    """Check the strength of many passwords from a file."""
    try:
        with open(password_file, 'r') as passwords:  # Open the file with passwords
            for password in passwords:
                password = password.strip()  # Clean the password of extra spaces
                result = zxcvbn(password)  # Get the password strength analysis
                entropy = calculate_entropy(password)  # Calculate the entropy

                # Prepare output to show for each password
                output = (
                    f"\n[+] ######################\n"
                    f"Value: {result['password']}\n"
                    f"Password Score: {result['score']}/4\n"
                    f"Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}\n"
                    f"Entropy (bits): {entropy:.2f}\n"
                    f"Feedback: {', '.join(result['feedback']['suggestions']) if result['feedback']['suggestions'] else 'None'}\n"
                )
                print(output)  # Display the results for this password

                # If an output file is provided, save the result to that file
                if output_file:
                    with open(output_file, 'a') as file:
                        file.write(output + '\n')
    except FileNotFoundError:
        print('[!] File not found. Please provide a valid file path.')  # Error message if file is missing

if __name__ == "__main__":
    # Check command-line arguments for file input/output
    if len(sys.argv) == 3:  # Format: script.py <input_file> <output_file>
        test_multiple_passwords(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:  # Format: script.py <input_file>
        test_multiple_passwords(sys.argv[1])
    elif len(sys.argv) == 1:  # No arguments -> single password
        output_file = input("Enter output file name (or press Enter to skip): ").strip()  # Ask for output file name
        test_single_password(output_file if output_file else None)
    else:
        print('Usage:\n'
              '  python check_password_strength.py <file> [output_file]\n'
              '  python check_password_strength.py\n'
              'Note: Use the second format for a single password test.')  # Print usage instructions