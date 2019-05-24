def sum_of_numbers(list_of_num,filter_func=None):
    sum=0
    if(filter_func==None):
        for i in list_of_num:
            sum+=i
    else:
        s=[]
        s=filter_func(list_of_num)
        for i in s:
            sum+=i
    return sum

def even(data):
    ev=[]
    for i in data:
        if(i%2==0):
            ev.append(i)
    return ev

def odd(data):
    od=[]
    for i in data:
        if(i%2!=0):
            od.append(i)
    return od

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
