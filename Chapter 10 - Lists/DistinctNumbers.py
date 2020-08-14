list1 = input("Enter ten numbers: ")
list2 = list1.split()
list3 = list()
for i in list2:
    # if list3.count(i) == 0:
    if i not in list3:
        list3.append(i)
print("The distinct numbers are:", end=" ")
for i in list3:
    print(i, end=" ")


'''
Enter ten numbers: 1 2 3 4 2 3 4 5 6 7
The distinct numbers are: 1 2 3 4 5 6 7 
Process finished with exit code 0
'''