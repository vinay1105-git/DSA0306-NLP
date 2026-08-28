import re
text = "DSA03 CSA17 MLA02 ITA04"
match = re.search(r"MLA02", text)
if match:
    print("Match Found.")
else:
    print("Match Not Found.")

