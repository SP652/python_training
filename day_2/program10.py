import sys

states=[]
capitals=[]


def split_states():
      argument=sys.argv[i]
      indexofspace=argument.find(' ')
      states.append(argument[:indexofspace])
      capitals.append(argument[:indexofspace+1:])
      
      
print('%-15s %s'%(states,capitals))
print('-'*27)
# i-0
# while states:
#       try and except statement from 