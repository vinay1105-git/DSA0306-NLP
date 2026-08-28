class PorterStemmer_Step3:

    def __init__(self):
        self.rules = {
            "icate" : "ic",
            "ative" : "",
            "alize" : "al",
            "iciti" : "ic",
            "ical" : "ic",
            "ful" : "",
            "ness" : ""
        }

    def ps_step3(self, word):
        for suffix, replacement in self.rules.items():
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                return stem + replacement
            
        return word

ps = PorterStemmer_Step3()

text = input("Enter a word or sentence: ")

words = text.split()

print("word\t\tStep_3_Stemword")
print("-"*30)

for word in words:
    stem = ps.ps_step3(word)
    print(f"{word:16}{stem}")