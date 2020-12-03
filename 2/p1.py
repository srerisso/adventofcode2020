import re

# Open File "input.txt"
with open('input.txt', 'r') as reader:
    # Read numbers less than 2020 into List
    n = []
    for line in reader.readlines():
        print(line, end='\n')

# regex : data
# check if data satisfies regex expression.
# return number of valid passwords.
