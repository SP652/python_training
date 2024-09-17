# Find the second smallest digit in a number

input_number=int(input('Enter the number '))

smallest_digit=9
second_smallest_digit=9
temp_number=input_number

while temp_number!=0:
    remainder_digit=temp_number%10
    temp_number=temp_number//10
    if remainder_digit<smallest_digit:
        second_smallest_digit=smallest_digit
        smallest_digit=remainder_digit
    elif remainder_digit< second_smallest_digit:
        second_smallest_digit = remainder_digit
print(f'Second smallest digit in {input_number} is {second_smallest_digit}')
