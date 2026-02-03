import random
import string

while True:
    print("\n*** PASSWORD GENERATOR ***")

    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print("Generated Password:", password)

    choice = input("Generate another password? (yes/no): ").lower()
    if choice != "yes":
        print("Program exited. Thank you!")
        break
