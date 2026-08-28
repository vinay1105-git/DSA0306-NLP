import re

email = input("Enter Email: ")
password = input("Enter Password: ")

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.([a-zA-Z]{2,})$"

password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*]).{8,}$"

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")