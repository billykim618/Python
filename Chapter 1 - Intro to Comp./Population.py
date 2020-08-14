CURRENT = 312032486
birth = 60 * 60 * 24 * 365 // 7
death = 60 * 60 * 24 * 365 // -13
immigrant = 60 * 60 * 24 * 365 // 45

addPop = birth + death + immigrant

print("Year 1 population:", CURRENT + addPop)
print("Year 2 population:", CURRENT + addPop * 2)
print("Year 3 population:", CURRENT + addPop * 3)
print("Year 4 population:", CURRENT + addPop * 4)
print("Year 5 population:", CURRENT + addPop * 5)
