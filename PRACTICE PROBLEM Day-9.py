***************************************** PROBLEM 45:***********************************************
from difflib import SequenceMatcher
def longest_common_substring(str1, str2):
    #start writing your code here
    match=SequenceMatcher(None,str1,str2).find_longest_match(0, len(str1), 0, len(str2)) 
    if (match.size!=0): 
	    return (str1[match.a: match.a + match.size]) 
    else: 
	    return("") 
output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)







from difflib import SequenceMatcher 
str1 = input()
str2 = input()
match=SequenceMatcher(None,str1,str2).find_longest_match(0, len(str1), 0, len(str2)) 
if (match.size!=0): 
	print (str1[match.a: match.a + match.size]) 
else: 
	print ("") 


	
