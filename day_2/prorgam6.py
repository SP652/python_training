#index Method- raises error in unsuccessful case
place = 'shivamogga'

print(place.index('shiva')) #0
print(place.index('mogga')) #5
print(place.index('mogga',2)) #5
print(place.index('mogga',2,7)) # start at 2 and end at 7 so result is -1(false)
print(place.index('mogga',4,10)) # 5
print(place.index('mogga',4,9)) #-1
print(place.index('kerala',0,10)) #-1


