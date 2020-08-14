# set1 = {"r", "a", "a", "q", "x"}
# print(set1)
# print("r" in set1)
# list1 = [1, 2, 3]
# print(3 in list1)
# set2 = set()
#
# dict1 = {}
# dict1 = {"joe":23, "jack":30}
# dict1["john"] = 4
#
# print(dict1)
# dict1["joe"] = 55
# print(dict1)
#
# tuple1 = (1, 2, 3)
# tuple2 = (5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3)
# print(tuple1 + 2)


list1 = ["Z", "A", "A", "B", "C"]
# set1.add(i)
# list1 = list(set1)
# list1.sort()
# print(list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
list2.sort()
print(list2)