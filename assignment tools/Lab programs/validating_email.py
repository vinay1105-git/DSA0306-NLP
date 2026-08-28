import re

pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.([a-zA-Z]{2,})$")

emails = [
    "Raj123@gmail.com",
    "Ram@college.edu",
    "Ramu@yahoo.in",
    "Rama@email",
    "Raja@.com"
]

for email in emails:
    if pattern.match(email):
        print(email, "- Valid Email")
    else:
        print(email, "- Invalid Email")