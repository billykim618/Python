number = eval(input("Enter a number between 0 and 1000: "))
answer = 0
# num1 = number % 10 # Isolate first digit of number by getting remainder after dividing by 10
# number //= 10 # Get rid of the first digit by integer division by 10. Same as number = number // 10
# num2 = number % 10
# number //= 10
# num3 = number % 10
#
# print("The sum of the digits is " + str(num1 + num2 + num3))

while number > 0:
    num1 = number % 10
    answer += num1
    number //= 10

print(answer)