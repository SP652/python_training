# Accept a number form the suer and chcek if it is a perfect square
import math

input_number=int(input('Enter the number to check if it is a perfect square '))

root_number=math.floor(math.sqrt(input_number))

if root_number*root_number == input_number:
    print(f'{input_number} is a perfect Square')
else:
    print(f'{input_number} is Not a perfect square')