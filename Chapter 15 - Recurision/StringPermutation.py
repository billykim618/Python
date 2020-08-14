def display_permutation(s):
    display_permutation_helper("", s)


def display_permutation_helper(s1, s2):
    if len(s2) == 0:
        print(s1)
        return

    for i in range(len(s2)):
        display_permutation_helper(s1 + s2[i], s2[:i] + s2[i+1:])


def main():
    s = input("Enter a string: ")
    display_permutation(s)


main()

'''
Enter a string: abc
abc
acb
bac
bca
cab
cba

Enter a string: abcd
abcd
abdc
acbd
acdb
adbc
adcb
bacd
badc
bcad
bcda
bdac
bdca
cabd
cadb
cbad
cbda
cdab
cdba
dabc
dacb
dbac
dbca
dcab
dcba
'''
