import re

def howManyCharsInPassw(c, str):
    return str.count(c)


def searchPolicyRange(str):
    regex = "\d+,\d+"
    result1 = re.search(regex,str)
    pol = result1.group(0)
    return pol

def isPolicyOk(ran1, ran2, car, str):
    # if (a and not b) or (not a and b)
    if (str[ran1] == car) and (str[an2] != car) ):
        return True
    if (str[ran2] == car):
        return True
    else:
        return False

# Open File "input.txt"
with open('input.txt', 'r') as reader:
    # Read all input data and put it in a list
    inputlist = []
    for line in reader.readlines():
        inputlist.append(line.rstrip())

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
#    result = howManyCharsInPassw(c,datainput)

    regexinput2 = regexinput.split()
    print(regexinput, datainput, range1, range2, c, isPolicyOk(int(range1), int(range2), c, datainput))
#    if (result in range(int(range1), int(range2)+1)): # ranbe2 tiene que sumar 1 para incluirlo
#        count += 1

print(count)