def reverse(number):
    new = 0
    while number > 0:
        new = (new * 10) + number % 10
        number //= 10
    return new


def isPalindrome(number):
    return number == reverse(number)


print(isPalindrome(111))
print(isPalindrome(123))
print(isPalindrome(123454321))
print(isPalindrome(11111111111111))