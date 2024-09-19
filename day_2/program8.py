#find the sum of the numbers entered via the command line

import sys


numbers=sys.argv
sum=0
for i in range(1,len(numbers)):
    sum+= float(numbers[i])

print(f'Sum = {sum}')