list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum=0 
    ag=0 
    c=0 
    for i in range(0,len(list_of_marks)):
        sum=sum+list_of_marks[i]
    ag=sum/len(list_of_marks)
    for i in range(len(list_of_marks)):
        if(ag<list_of_marks[i]):
            c=c+1
    per=(c/len(list_of_marks))*100
    return (per)

def sort_marks():
    lis=sorted(list_of_marks)
    return(lis)

def generate_frequency():
    l=[]
    for i in range(0,26):
        c1=0 
        for j in range(0,len(list_of_marks)):
            if(list_of_marks[j]==i):
                c1=c1+1
        l.append(c1)
    return(l)
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
