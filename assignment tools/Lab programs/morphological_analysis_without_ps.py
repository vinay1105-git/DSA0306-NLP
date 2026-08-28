import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# Input sentence
text = "The boys are running, the girls are writing letters, and the children played games."

# Tokenize the sentence
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Function to convert NLTK POS tags to WordNet POS
from nltk.corpus import wordnet

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

print("Word\t\tPOS\tLemma")
print("-" * 35)

# Perform Morphological Analysis
for word, tag in pos_tags:
    lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    print(f"{word:16}{tag:8}{lemma}")
