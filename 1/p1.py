
def sum2end(list):
    list2 = list.pop()
    list3 = []
    for i in list:
        list3.append(i+list2)

    return list3

# Open File "puzzle1_input.txt"
with open('puzzle1_input.txt', 'r') as reader:
    # Read numbers less than 2020 into List
    n = []
    for line in reader.readlines():
        n.append(int(line))

# Search starting from position 1

# if pos[i] + pos[j] = 2020 then result = pos[i] * pos[j]
# return results
results = []
n2 = n

for i in n:
    for j in n2:
        #results = append(i)
        if (i != j):
            if (i+j == 2020):
                print(i)
                print(j)
                print(i*j)
else:
    print("Completed succesfully")

