def main():
    f1 = input("Enter a source filename: ").strip()
    f2 = input("Enter a target filename: ").strip()

    s = open(f1)
    s3 = open(f2, "w")
    s1 = s.read()
    list1 = []

    s5 = ""
    for i in s1:
        # list1.append(chr(ord(i) + 5))
        s5 += (chr(ord(i) + 5))


# print(list1)
#     s2 = ''.join(list1)
#     print(s2)
#     s3.write(s2)

    print(s5)
    s3.write(s5)

    s.close()
    s3.close()



main()


'''
Enter a source filename: Presidents.txt
Enter a target filename: Encrypted.txt
['G', 'n', 'q', 'q', '%', 'H', 'q', 'n', 's', 'y', 't', 's', '\x0f', 'L', 'j', 't', 'w', 'l', 'j', '%', 'G', 'z', 'x', 'm', '\x0f', 'G', 'f', 'w', 'f', 'h', 'p', '%', 'T', 'g', 'f', 'r', 'f']
Gnqq%HqnsytsLjtwlj%GzxmGfwfhp%Tgfrf
'''
