import urllib.request


def main():
    infile = urllib.request.urlopen("http://www.w3.org/TR/PNG/iso_8859-1.txt")
    s = infile.read().decode()

    counts = countLetters(s.lower())

    # Display results
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i])
                  + (" time" if counts[i] == 1 else " times"))


def countLetters(s):
    counts = 26 * [0]  # Create and initialize counts
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
    return counts


main()


'''
a appears 337 times
b appears 46 times
c appears 185 times
d appears 93 times
e appears 465 times
f appears 59 times
g appears 67 times
h appears 98 times
i appears 298 times
j appears 2 times
k appears 17 times
l appears 372 times
m appears 97 times
n appears 107 times
o appears 87 times
p appears 89 times
q appears 12 times
r appears 246 times
s appears 165 times
t appears 465 times
u appears 71 times
v appears 28 times
w appears 64 times
x appears 19 times
y appears 14 times
z appears 3 times
'''

