input_score=int(input('Enter the score '))
if input_score<0 or input_score>100:
    print('Invalid Input')
else:
    if input_score>=90:
        print('Distinction')
    elif input_score>=75:
        print(' FC')
    elif input_score>=50:
        print('SC')
    else:
        print('Fail')