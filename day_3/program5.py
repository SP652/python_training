def calc(fisrt_num:int,second_num:int) ->int:
    sum=fisrt_num+second_num
    difference=fisrt_num-second_num
    product=fisrt_num*second_num
    quotient=fisrt_num//second_num
    return sum,difference,product,quotient

s,d,p,q=calc(24,8)

print(s,d,p,q)

t1=calc(35,7)
print(t1)