def isAnagram(s1, s2):
    # Convert the two strings, s1 and s2, into list1 and list2, respectively.
    list1 = list(s1)
    list1.sort()
    list2 = list(s2)
    list2.sort()
    # Return True or False depending on if they are the same list when sorted.
    return list1 == list2


def main():
    s1 = input("Enter a word: ")
    s2 = input("Enter a word: ")
    print()  # Print blank line
    print(s1, "and", s2, "are anagrams.") if isAnagram(s1, s2) else print(s1, "and", s2, "are not anagrams.")


main()

'''
Enter a word: listen
Enter a word: silent

listen and silent are anagrams.

Enter a word: hello
Enter a word: goodbye

hello and goodbye are not anagrams.

Enter a word: abcdefghijklmnopqrstuvwxyz
Enter a word: zyxwvutsrqponmlkjihgfedcba

abcdefghijklmnopqrstuvwxyz and zyxwvutsrqponmlkjihgfedcba are anagrams.
'''