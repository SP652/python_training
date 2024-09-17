# Print the Math table of a number upto multiples of 20

input_number=int(input('Enter the number to obtain the math table '))

end_number=20
for i in range (1,end_number+1):
    print('%d * %02d = %3d'%(input_number,i,input_number*i))
