
import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(
        secrets.choice(characters) for _ in range(length)
    )
    return password

def main():
    print("=" * 35)
    print("       PASSWORD GENERATOR")
    print("=" * 35)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Please enter a length of at least 8.")
                continue

            if length > 128:
                print("Password length cannot exceed 128.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    password = generate_password(length)

    print("\nGenerated Password:", password)
    print("Password Length:", len(password))
    print("\nPassword generated successfully!")

if __name__ == "__main__":
    main()
