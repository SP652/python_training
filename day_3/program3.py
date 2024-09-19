my_list=[2,3,5,7,11]

print(my_list)

my_list[0::2]=(e**2 for e  in my_list[0::2])
my_list[1::2]=(e**3 for e  in my_list[1::2])

print(my_list)