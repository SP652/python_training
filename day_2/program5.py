# Find method

place = 'shivamogga'

print(place.find('shiva')) #0
print(place.find('mogga')) #5
print(place.find('mogga',2)) #5
print(place.find('mogga',2,7)) # start at 2 and end at 7 so result is -1(false)
print(place.find('mogga',4,10)) # 5
print(place.find('mogga',4,9)) #-1
print(place.find('kerala',0,10)) #-1


