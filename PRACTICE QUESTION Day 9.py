***************PROBLEM 6:************
def list123(nums):
    for i in range(0,len(nums)):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True 
        else:
            return False

nums=[1,2,1,4,3]
print(list123(nums))



****************PROBLEM 7:***********
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
