list1 = []
list2 = []

with open("db1.txt", "r") as file:
    for line in file:
        numbers = line.strip().split('   ')
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))


#sort arrays

list1.sort()
list2.sort()
similarityScore = {num: list2.count(num) for num in list1}

totalDistance = 0
for y in range(len(list1)):
    totalDistance = totalDistance + abs((list2[y] - list1[y]))

totalScore  = 0
for x in similarityScore:
    totalScore = totalScore + (x * similarityScore[x])
print(list1[2])
print(list2[2])
print(totalDistance)
print(totalScore)