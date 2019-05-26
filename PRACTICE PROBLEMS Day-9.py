********************************PROBLEM 26:***************************
def check_occurence(string):
    c1=0
    c2=0
    c=string.lower()
    c1=c.count("jet")
    c2=c.count("mat")
    if(c1==c2):
        return True
    else:
        return False
string="Jet on the Mat but mat is too long"
print(check_occurence(string))




******************************PROBLEM 27:**************************************
 def check_for_ten(num1,num2):
    if(num1 ==10 or num2 ==10):
        return True 
    elif num1+num2==10:
        return True 
    else:
        return False
    
print(check_for_ten(10,9))   
    
    
    
**************************PROBLEM 28:****************************************
   def sing_99_bottles():
   for i in range(99,-1,-1):
       print(str(i)+"bottles of beer on the wall"+str(i)+"bottles of beer."+"\n"+
             "Take one down, pass it around,"+str(i-1)+" bottles of beer on the wall.")
sing_99_bottles()



*****************************PROBLEM 29:*************************************
    def exchange_list(number_list):
    l=[]
    s=[]
    k=len(number_list)//2
    for i in range(0,k):
        l.append(number_list[i])
    for i in range(k,len(number_list)):
        s.append(number_list[i])
        s.sort(reverse=True)
    number_list=s+l
    return number_list
     
number_list=[1,2,3,4,5,6,7,8,9,10]
print(exchange_list(number_list))




*****************************PROBLEM 30:*****************************************8
   
#Provide different values for limit and t
