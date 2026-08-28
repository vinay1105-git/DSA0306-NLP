class porter_stemmer:

    def __init__(self):

        self.step_1a_rules={
            # STEP 1A RULES
            "sses" : "ss",
            "ies"  : "i",
            "ss"   : "ss",
            "s"    : ""
        }

        self.step_2_rules={
            # STEP 2 RULES
            "ational" : "ate",
            "tional" : "tion",
            "enci" : "ence",
            "anci" : "ance",
            "izer" : "ize",
            "abli" : "able",
            "alli" : "al",
            "entli" : "ent",
            "eli" : "e",
            "ousli" : "ous",
            "ization" : "ize",
            "ation" : "ate",
            "ator" : "ate",
            "alism" : "al",
            "iveness" : "ive",
            "fulness" : "ful",
            "ousness" : "ous",
            "aliti" : "al",
            "iviti" : "ive",
            "biliti" : "ble"
        }


        self.step_3_rules={
            # STEP 3 RULES
            "alize" : "al",
            "ative" : "",
            "ful"   : "",
            "iciti" : "ic",
            "icate" : "ic",
            "ical"  : "ic",
            "ness"  : ""
        }

        self.step_4_rules={
            # STEP 4 RULES
            "al" : "",
            "ance" : "",
            "ence" : "",
            "er"   : "",
            "ic"   : "",
            "able" : "",
            "ible" : "",
            "ant"  : "",
            "ement": "",
            "ment" : "",
            "ent"  : "",
            "ou"   : "",
            "ism"  : "",
            "ate"  : "",
            "iti"  : "",
            "ous"  : "",
            "ive"  : "",
            "ize"  : ""
        }

    
    def step_1a(self, word):
        for suffix,replace in self.step_1a_rules.items():
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                return stem + replace
        return word
        
    def step_1b(self, word):
        if word.endswith("eed"):
            stem = word[:-3]
            if self.m_value(stem)>0:
                return stem + "ee"

        elif word.endswith("ed"):
            stem = word[:-2]
            if self.contain_vowels(stem):
                word = stem

        elif word.endswith("ing"):
            stem = word[:-3]
            if self.contain_vowels(stem):
                word = stem
        else:
            return word

        if word.endswith(("at","bl","iz")):
            return word + "e"

        elif self.double_consonant(word):
            if word[-1] not in "lsz":
                return word[:-1]

        elif self.m_value(word)==1 and self.cvc(word):
            return word + "e"
        return word

    def step_1c(self, word):
        if word.endswith("y"):
            stem = word[:-1]
            if self.contain_vowels(stem):
                return stem + "i"
        return word

    def step_2(self, word):
        for suffix,replace in self.step_2_rules.items():
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.m_value(stem)>0:
                    return stem + replace
        return word

    def step_3(self, word):
        for suffix,replace in self.step_3_rules.items():
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.m_value(stem)>0:
                    return stem + replace
        return word

    def step_4(self, word):
        for suffix,replace in self.step_4_rules.items():
            if word.endswith(suffix):
                stem = word[:-len(suffix)]
                if self.m_value(stem)>1:
                    return stem + replace

        if word.endswith("ion"):
            stem = word[:-3]
            if self.m_value(stem)>1:
                if stem.endswith(("s","t")):
                    return stem
        return word

    def step_5a(self, word):
        if word.endswith("e"):
            stem = word[:-1]
            if self.m_value(stem)>1:
                return stem
            else:
                if self.m_value(stem)==1:
                    if not self.cvc(stem):
                        return stem
                    return word
                return word
        return word
    
    def step_5b(self, word):
        if self.m_value(word)>1 and self.double_consonant(word) and word.endswith("ll"):
                    return word[:-1]
        return word



    def m_value(self, stem):
        output = self.convert(stem)
        result = self.remove_repeate(output)
        m = result.count("vc")
        return m

    def convert(self, stem):
        pattern = ""
        for i in range(len(stem)):
            if self.vowel(stem,i):
                pattern += "v"
            else:
                pattern += "c"
        return pattern
    

    def vowel(self, stem, i):
        if stem[i] in "aeiou":
            return True
        if stem[i] == "y":
            if i == 0:
                return False
            elif stem[i-1] in "aeiou":
                return False
            else:
                return True
        return False

    def remove_repeate(self, output):
        if output == "":
            return ""
        result = output[0]
        for i in range(1,len(output)):
            if output[i]==output[i-1]:
                continue
            else:
                result +=output[i]
        return result
    
    def contain_vowels(self, stem):
        for i in range(len(stem)):
            if self.vowel(stem, i):
                return True
        return False

    def double_consonant(self, stem):
        if len(stem)>=2:
            if stem[-1] == stem[-2]:
                if self.vowel(stem, -1):
                    return False
                return True
            return False
        return False

    def cvc(self, stem):
        if len(stem)>=3:
            if not self.vowel(stem, -1):
                if self.vowel(stem, -2):
                    if not self.vowel(stem, -3):
                        if stem[-1] not in "wxy": 
                            return True
                        return False
                    return False
                return False
            return False
        return False

        
    def op_ip(self, word):
        word = self.step_1a(word)
        word = self.step_1b(word)
        word = self.step_1c(word)
        word = self.step_2(word)
        word = self.step_3(word)
        word = self.step_4(word)
        word = self.step_5a(word)
        word = self.step_5b(word)
        return word

ps = porter_stemmer()

text = input("Enter the Word: ").lower()

words = text.split()

print("Word\t\t\tStem_Word")
print("-"*30)

for word in words:
    stem = ps.op_ip(word)
    print(f"{word:24}{stem}")
