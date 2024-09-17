# Read a number from the user and print the lucky digit of the user where the lucky digit is found by finding the sum of digits 
# of the givetemp_numbernumber and repeat the algorithm until single digit number is arrived


input_number=int(input('Enter the number to find the lucky number '))
while input_number >= 10:
    temp = input_number
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    
    input_number = digit_sum

print(f"The lucky digit of the number is: {input_number}")