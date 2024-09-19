# Number of occurences of the numbers provided by the user
numbers=input('Enter the numbers').split()
frequency_dict={}
for num in numbers:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1
print(frequency_dict)
