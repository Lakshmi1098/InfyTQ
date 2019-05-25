**********************PROBLEM 6:********************
def list123(nums):
    for i in range(0,len(nums)):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True 
        else:
            return False

nums=[1,2,1,4,3]
print(list123(nums))



***********************PROBLEM 7:*******************
def seed_no(number,ref_no):
    n=[int(x) for x in str(number)]
    product=1
    for i in range(0,len(n)):
        product+product*n[i]
    s=product*number
    if(s==ref_no):
        return True
    else:
        return False
number=123
ref_no=738
print(seed_no(number,ref_no))



************************PROBLEM 8:*****************
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=='D'):
            net_amount+=int(a[1])
        else:
            net_amount-=int(a[1])
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))



*********************PROBLEM 9:********************
def generate_dict(number):
	l1=[]
	l2=[]
	for i in range(1,number+1):
	    l1.append(i)
	for i in range(1,number+1):
	    l2.append(i**2)
	dic=dict(zip(l1,l2))
	
	return str(dic)

number=10
print(generate_dict(number))



******************PROBLEM 10:******************
def find_upper_and_lower(sentence):
    c1=0
    c2=0
    result_list=[]
    for i in sentence:
        if i.islower():
            c1=c1+1
        elif i.isupper():
            c2=c2+1
    result_list.append(c2)
    result_list.append(c1)
    return result_list

sentence="Welcome to Mysore"
print(find_upper_and_lower(sentence))
