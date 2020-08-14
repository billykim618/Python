def reverse(s):
    i = -1  # Initialize i to be -1 which is the index of the last character of a string (-1 + len(s))
    newString = ""  # Initialize newString to be an empty string

    while i >= -len(s):  # Until i reaches the length of the string:
        newString += (s[i])  # Appends character at s[i] to newString
        i -= 1  # Decrement i by 1 to traverse through string backwards

    return newString


def main():
    s = input("Enter a word: ")
    print("The reverse of", s, "is", reverse(s))


main()


'''

Enter a word: noon
The reverse of noon is noon

Process finished with exit code 0

Enter a word: ABCDEFG
The reverse of ABCDEFG is GFEDCBA

Process finished with exit code 0

Enter a word: ABC123!@#
The reverse of ABC123!@# is #@!321CBA

Process finished with exit code 0

'''