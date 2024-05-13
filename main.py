# password Manager
# Website/Email (123@gmail.com)
# Password 123456

# importing model
import os
import random
from cryptography.fernet import Fernet
import questionary

print("Welcome To Password Manager")

if not (os.path.exists("key.key")):
    key = Fernet.generate_key()

    with open("key.key", "wb") as file:
        file.write(key)

        if not (os.path.exists("passwords.txt")):
            with open("passwords.txt", "w") as file:
                pass

if os.path.exists("pin.txt"):
    with open("pin.txt", "r") as file:
        code = file.read()

    user_code = input("\nEnter the code: ")

    if user_code == code:
        print()
        user_input = questionary.select("Chose any one of the following:", choices =["Add a password", "View stored passwords"]).ask()

        if user_input == "Add a password":
            # Adding Password to the file
            website = input("\nEnter the website name/email to store:")
            password = questionary.password("Enter the password to store: ").ask()

            # Encrypt the password and store it in the file
            with open("key.key", "rb") as file:
                key = file.read()
                cipher = Fernet(key)

            encrypted_password = cipher.encrypt(password.encode()).decode()

            with open("password.txt", "a") as file:
                file.write(f"{website}||{encrypted_password}\n")

            print("Password Added Successfully")

        else:
            # Viewing stored passwords
            with open("key.key", "r") as file:
                file_lines = file.readlines()

                if file_lines:
                    for index, line in enumerate(file_lines):
                        line = line.strip()
                        user_website, user_password = line.split("||")

                        with open("key.key", "rb") as file:
                            key = file.read()

                        cipher = Fernet(key)
                        decrypted_password = cipher.decrypt(user_password.encode()).decode()

                        print(f"\n{index+1}) Website/Email: {user_website}\npassword: {decrypted_password}")
                    print()

                else:
                    print("No stored password!")

    else:
        print("Incorrect code!")

else:
    code = str(random.randint(1000, 2000))

    with open("pin.txt", "w") as file:
        file.write(code)

    print(f"\nYour code to enter the application is {code}")
    print("you will be shown this code only once.")

    user_code = input("\nEnter the code: ")

    if user_code == code:
        print()
        user_input = questionary.select("Chose any one of the following:", choices =["Add a password", "View stored passwords"]).ask()

        if user_input == "Add a password":
            # Adding Password to the file
            website = input("\nEnter the website name/email to store:")
            password = questionary.password("Enter the password to store: ").ask()

            # Encrypt the password and store it in the file
            with open("key.key", "rb") as file:
                key = file.read()
                cipher = Fernet(key)

            encrypted_password = cipher.encrypt(password.encode()).decode()

            with open("password.txt", "a") as file:
                file.write(f"{website}||{encrypted_password}\n")

            print("Password Added Successfully")

        else:
            # Viewing stored passwords
            with open("Passwords.txt", "r") as file:
                file_lines = file.readlines()

                if file_lines:

                    for index, line in enumerate(file_lines):
                        line = line.strip()
                        user_website, user_password = line.split("||")

                        with open("key.key", "rb") as file:
                            key = file.read()

                        cipher = Fernet(key)
                        decrypted_password = cipher.decrypt(user_password.encode()).decode()

                        print(f"\n{index+1}) Website/Email: {user_website}\npassword: {decrypted_password}")

                    print()

                else:
                    print("No sored passwords!")

    else:
        print("Incorrect code!")