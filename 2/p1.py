import re

def howManyCharsInPassw(c, str):
    return str.count(c)


def searchPolicyRange(str):
    regex = "\d+,\d+"
    result1 = re.search(regex,str)
    pol = result1.group(0)
    return pol

# Open File "input.txt"
with open('input.txt', 'r') as reader:
    # Read all input data and put it in a list
    inputlist = []
    for line in reader.readlines():
        inputlist.append(line.rstrip())

# We have 
#   regex : data
# We should check if 'data' satisfies 'regex' expression
# and return number of valid passwords (that satisfy 'regex').

# 1. Convert 'regex' in input data to Python regex format
# n1-n2 l  => l{n1-n2}

# for loop to convert regex expression to Python format
"""newinputlist = []
for i in inputlist:
    regexinput = i.split(':')[0].replace('-',',')
    datainput = i.split(':')[1]
    regexinput2 = regexinput.split()
    newregex = regexinput2[1]+'{'+regexinput2[0]+'}'
    newinputlist.append((newregex,datainput))

#print(newinputlist)

count = 0
# j[0] is regexp part (l{4,5})
# \d+,\d+ matches the part between llaves
# j[1] is text string part (rllllj)

for j in newinputlist:
    # primero, obtenemos cuantos caracteres hay en la contraseña
    result = howManyCharsInPassw(j[0][0], j[1])
    # segundo, determinamos la policy del password
    policy = searchPolicyRange(j[0])
    # tercero, comprobamos si result está en el rango que determina la policy
#    if (result in range(int(policy[0]),int(policy[2]))):
#        count += 1
"""

count = 0

for i in inputlist:
    regexinput = i.split(':')[0]
    range1 = regexinput.split('-')[0]
    range2Andc = regexinput.split('-')[1]
    range2 = range2Andc.split()[0]
#    print(range2)
    c = range2Andc.split()[1]
#    print(c)
    datainput = i.split(':')[1]
    result = howManyCharsInPassw(c,datainput)

    regexinput2 = regexinput.split()
    print(regexinput, datainput, range1, range2, result, result in range(int(range1), int(range2)+1))
    if (result in range(int(range1), int(range2)+1)): # range2 tiene que sumar 1 para incluirlo
        count += 1

print(count)