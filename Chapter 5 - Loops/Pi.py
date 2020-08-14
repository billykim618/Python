q = 0
for i in range(1, 11):
    pi = 0
    for x in range(10000 * i, 0, -1):
        pi += (((-1) ** (x + 1)) / (2 * x - 1))
    pi *= 4
    q += 10_000
    print("Pi =", pi, " when x =", q)
    i += 1

'''
Pi = 3.1414926535900434  when x = 10000
Pi = 3.1415426535898248  when x = 20000
Pi = 3.1415593202564693  when x = 30000
Pi = 3.141567653589797  when x = 40000
Pi = 3.1415726535897956  when x = 50000
Pi = 3.1415759869231277  when x = 60000
Pi = 3.1415783678755087  when x = 70000
Pi = 3.141580153589794  when x = 80000
Pi = 3.141581542478683  when x = 90000
Pi = 3.1415826535897935  when x = 100000

Process finished with exit code 0
'''