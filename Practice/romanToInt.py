def romanToInt(s: str) -> int:
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    for i in range(len(s)):
        num += dictionary.get(s[i])
        if len(s) == 1:
            break
        if i == 0:
            continue
        if (s[i] == "V" or s[i] == "X") and s[i - 1] == "I":
            num -= 2
        if (s[i] == "L" or s[i] == "C") and s[i - 1] == "X":
            num -= 20
        if (s[i] == "D" or s[i] == "M") and s[i - 1] == "C":
            num -= 200
    print(num)

romanToInt("MMMCDXC")