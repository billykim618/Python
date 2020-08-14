def merge(list1, list2):
    for i in range(len(list1)):
        list1[i] = eval(list1[i])
    for i in range(len(list2)):
        list2[i] = eval(list2[i])
    list3 = list1 + list2
    list3.sort()

    print("The merged list is", end=" ")
    for i in range(len(list3)):
        print(list3[i], end=" ")


def main():
    input1 = input("Enter list1: ")
    input2 = input("Enter list2: ")
    list1 = input1.split()
    list2 = input2.split()

    merge(list1, list2)


main()


'''
Enter list1: 1 5 16 61 111
Enter list2: 2 4 5 6
The merged list is 1 2 4 5 5 6 16 61 111 

Enter list1: 12 13 14 15
Enter list2: 1 2 3 4
The merged list is 1 2 3 4 12 13 14 15 
'''