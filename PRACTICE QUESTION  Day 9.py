******************** PROBLEM 21:******************


********************PROBLEM 22:*****************
def diagonal_stars(number):
    for i in range(0,number+1):
        for j in range(i):
            print(".",end="")
        print("*")
    

number=6    
diagonal_stars(number)



******************PROBLEM 23***********************
def divisible_by_sum(number):
    n=[int(x) for x in str(number)]
    if(number%sum(n)==0):
        return True
    else:
        return False
    
number=42
print(divisible_by_sum(number))




***************** PROBLEM 24:*******************
def find_gcd(num1,num2):
    from math import gcd
    return gcd(num1,num2)

num1=800
num2=2800
print(find_gcd(num1,num2))


******************* PROBLEM 25***************
def list_of_count(word_list):
    l=[]
    for i in range(0,len(word_list)):
        s=len(word_list[i])
        l.append(s)
    
    return l

word_list=["COme","here"]
print(list_of_count(word_list))
