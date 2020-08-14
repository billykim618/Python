def checkPassword(pw):
    if len(pw) >= 8:  # If the length of the pw is at least 8, continue, else return False
        if pw.isalnum():  # If pw is alphanumeric, continue, else return False
            count = 0  # Declare & initialize a count variable to count how many digits are in pw
            for i in range(len(pw)):
                if pw[i].isalpha():  # If pw[i] is a letter, do nothing, else if it's a digit, add 1 to count
                    count += 0
                else:
                    count += 1
            if count >= 2:  # If there are at least 2 digits, it has passed all 3 test, and is a valid password.
                return True
            else:
                print("Invalid password. Password did not contain at least 2 digits.")
                return False
        else:
            print("Invalid password. Password can only contain letters and digits.")
            return False
    else:
        print("Invalid password. Password was not at least 8 characters.")
        return False


def main():
    password = input("Enter your password: ")
    if checkPassword(password):
        print(password, "is a valid password.")


main()


'''
SAMPLE OUTPUT:
Enter your password: 12345
Invalid password. Password was not at least 8 characters.

Process finished with exit code 0

Enter your password: !!!!!!!!!!!
Invalid password. Password can only contain letters and digits.

Process finished with exit code 0

Enter your password: 0AAAAAAAAA
Invalid password. Password did not contain at least 2 digits.

Process finished with exit code 0

Enter your password: ABCD1234
ABCD1234 is a valid password.

Process finished with exit code 0
'''