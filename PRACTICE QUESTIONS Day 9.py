*******************PROBLEM 1:******************
def add_string(str1):
  #start writing your code here
  if(len(str1)>=3):
        if(str1.endswith("ing")):
            str1=str1+"ly"
        else:
            str1=str1+"ing"
  
  return str1

str1="com"
print(add_string(str1))

*******************PROBLEM  2:********************
  def bracket_pattern(input_str):
    c1=input_str.count('(')
    c2=input_str.count(')')
    if(input_str.startswith(')') or input_str.endswith('(')):
        return False
    elif(c1==c2):
        return True 
    else:
        return False
    

    
input_str="()((())())"
print(bracket_pattern(input_str))


************ PROBLEM 3:************************
  def create_new_dictionary(prices):
    new_dict={}
    for key in prices:
        if(prices[key]>200):
           new_dict.__setitem__(key,prices[key])
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))


************* PROBLEM 4:******************
  def find_nine(nums):
    for i in range(0,4):
        if(nums[i]==9):
            return True
    else:
        return False

nums=[1, 2,3,4]
print(find_nine(nums))



****************PROBLEM 5:******************
  def count_digits_letters(sentence):
    letters=0
    digit=0
    l=[]
    for i in sentence:
        if i.isalpha():
            letters += 1
           
        elif i.isnumeric():
            digit += 1
            
    l.append(letters)
    l.append(digit) 
    return l
sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
