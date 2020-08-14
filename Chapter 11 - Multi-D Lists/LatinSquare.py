import sys


def main():
    n = eval(input("Enter number n: "))
    print("Enter", n, "rows of letters separated by spaces:  ")
    # your work
    matrix = []  # Create list
    for row in range(n):
        matrix.append([])  # Append a list within 'matrix'
        value = input()  # Input letters to 'value'
        splitLetters = value.split()  # Split the letters into new list 'splitLetters'
        matrix[row] = [x for x in splitLetters]  # Assign each letter within 'splitLetters' to 'matrix[row]'
    print(matrix)

    print("The input list is a latin square") \
        if getTransposed(matrix) == matrix \
        else print("The input list is NOT a latin square")


def getTransposed(matrix):
    result = []

    for j in range(len(matrix)):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)

    return result


main()


'''
Enter number n: 4
Enter 4 rows of letters separated by spaces:  
A B C D
B A D C
C D B A
D C A B
[['A', 'B', 'C', 'D'], ['B', 'A', 'D', 'C'], ['C', 'D', 'B', 'A'], ['D', 'C', 'A', 'B']]
The input list is a latin square

Enter number n: 3
Enter 3 rows of letters separated by spaces:  
A B C
B C A
C A B
[['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']]
The input list is a latin square

Enter number n: 3
Enter 3 rows of letters separated by spaces:  
A B C
A B C
A B C
[['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']]
The input list is NOT a latin square
'''