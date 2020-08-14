keywords = ["and", "as", "assert", "break", "class", "continue",
            "def", "del", "elif", "else", "except", "False",
            "finally", "for", "from", "global", "if", "import", "in",
            "is", "lambda", "None", "nonlocal", "not", "or", "pass",
            "raise", "return", "True", "try", "while", "with", "yield"]

f = open("FindGenes.py")
f1 = open("FindGenes.py")
print("The Python source file:", f1.read())
list1 = f.read().split()

dict1 = {}
for word in list1:
    if word in keywords and word not in dict1:
        dict1[word] = 1
    elif word in dict1:
        count = dict1.get(word)
        dict1[word] = count + 1

print("The keywords and their count in the Python source file:", dict1)

f.close()
f1.close()
