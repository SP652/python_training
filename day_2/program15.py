


import sys

numbers = []

for i in range(1, len(sys.argv)):
    numbers.append(int(sys.argv[i]))

print(numbers)

strings=[str(element) for element in numbers]# for each loop is being used here
print(numbers)

