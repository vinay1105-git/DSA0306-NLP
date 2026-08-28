import re

text = input("Enter the text: ")

sentences = re.split(r"[.!?]+", text)

words = re.split(r"\s+", text.strip())

print("Sentences:", sentences)
print("Total Sentences:", len(sentences))

print("\nWords:", words)
print("Total Words:", len(words))