input_num1 = int(input('Enter the 1st number '))
input_num2 = int(input('Enter the 2st number '))
input_num3 = int(input('Enter the 3st number '))

if input_num1 > input_num2 and input_num1 > input_num3:
    print(f'Num1= {input_num1} is the biggest number')
elif input_num2 > input_num3:
    print(f'Num2= {input_num2} is the biggest number')
else:
    print(f'Num3= {input_num3} is the biggest number')

    