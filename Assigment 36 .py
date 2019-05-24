def create_largest_number(number_list):
    
    #remove pass and write your logic here
    ans=""
    number_list.sort()
    for i in range(len(number_list)-1,-1,-1):
        ans=ans+str(number_list[i])
        an=int(ans)
    return an    

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
