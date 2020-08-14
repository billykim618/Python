list1 = []
newDPlus = open("DPlusABC", "w")
file = open("DPlus2.txt", "r")
for line in file:
        list1.append(line)
list1.sort()
for x in list1:
        newDPlus.write(x)
        newDPlus.write("\n")