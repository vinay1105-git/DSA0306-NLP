# Word Stemming using Porter Stemmer

import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "running", "playing", "studies", "studying",
    "connected", "connection", "happiness",
    "flying", "wolves", "cars"
]

print("Original Word\t\tStemmed Word")
print("-" * 40)

# Perform stemming
for word in words:
    stem = stemmer.stem(word)
    print(f"{word:24}{stem}")
