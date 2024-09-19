list1=[3,23,19,11,13,5,17]


list2=[29,7,31]

list3=[43,41,47]

l1=[1,2,3]
l2=[1,2,3]

print(list1+list2)
print(list2>list1)


list1.extend(list2)
print(list1)

list2.insert(2,list3)
print(list2)

print(l1.__eq__(l2)) #check for objects and not references
print(l1==l2) 