def main():
    f1 = input("Enter a source filename: ").strip()
    f2 = input("Enter a target filename: ").strip()

    infile = open(f1, "r")
    s = infile.read()  # Read all from the file
    list1 = []

    print("Encrypted file is:", s)

    for i in s:
        list1.append(chr(ord(i) - 5))

    s1 = ''.join(list1)
    print("Decrypted file is:", s1)

    outfile = open(f2, "w")
    outfile.write(s1)

    infile.close()
    outfile.close()


main()


'''
Enter a source filename: Encrypted.txt
Enter a target filename: Decrypted.txt
Encrypted file is: Gnqq%HqnsytsLjtwlj%GzxmGfwfhp%Tgfrf
Decrypted file is: Bill Clinton
George Bush
Barack Obama
'''