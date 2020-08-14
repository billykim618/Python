import os.path

if os.path.isfile("GoodDay.txt"):
    input1 = input("Enter a file: ")

s = open(input1, "r")
s = s.read()
words = s.split()
print("The file reads:", words)
set1 = set(words)
print("After put into a set:", set1)
list = list(set1)
print("After put into a list:", list)
list.sort()
print("The list after sort:", list)


'''
Enter a file: GoodDay.txt
The file reads: ['This', 'is', 'such', 'a', 'good', 'day', 'Everyday', 'is', 'a', 'good', 'day']
After put into a set: {'day', 'This', 'good', 'Everyday', 'such', 'is', 'a'}
After put into a list: ['day', 'This', 'good', 'Everyday', 'such', 'is', 'a']
The list after sort: ['Everyday', 'This', 'a', 'day', 'good', 'is', 'such']

Process finished with exit code 0
'''