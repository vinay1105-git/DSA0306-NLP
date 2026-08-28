def generate_plural(noun):

    # State q0 (Start State)
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        # Transition to q1
        plural = noun + "es"

    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        # Transition to q2
        plural = noun[:-1] + "ies"

    else:
        # Transition to q3
        plural = noun + "s"

    return plural

text = input("Enter a singular noun:")

# Test words
words = text.split()

print("Singular\tPlural")
print("------------------------")

for word in words:
    print(f"{word:10}\t{generate_plural(word)}")