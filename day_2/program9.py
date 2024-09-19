#State and capital, cut state names form argv to state list and do the same for capital

import sys

states=[]
capitals=[]
#method 1
# for i in range(1, len(sys.argv), 2):
#         if i < len(sys.argv) - 1:
#             states.append(sys.argv[i])
#             capitals.append(sys.argv[i + 1])
# print("States:", states)
# print("Capitals:", capitals)


# Method 2 
# if input is as 'a b' 'c d'
for i in range (1, len(sys.argv)):
  arguments=sys.argv[i].split()
  states.append(arguments[0])
  capitals.append(arguments[1])

# Method 3
# def split_states():
#       argument=sys.argv[i]
#       indexofspace=argument.find(' ')
#       states.append(argument[:indexofspace])
#       capitals.append(argument[:indexofspace+1:])
#  for states, capitals in states,capitals:
#   print('%-15s %s'%(states[i],capital[i]]))

# FOR CASES WITH NO  ' ' TYPE OF DATA

# for i in range(1,len(sys.argv),2):
#     states.append(sys.argv[i])
#     capitals.append(sys.argv[i+1])

print("States:", states)
print("Capitals:", capitals)