def longestCommonPrefix(strs):
    if not strs:
        print("")
    str = ""
    strs = sorted(strs)
    for letter in range(len(strs[0])):
        compare = strs[0][letter]
        for i in range(1, (len(strs))):
            if compare != strs[i][letter]:
                print(str)
        str += compare
    print(str)

longestCommonPrefix(["aa", "a"])

