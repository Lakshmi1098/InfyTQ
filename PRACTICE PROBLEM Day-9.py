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

********************************************************PROBLEM 17:*******************************************
#PF-Prac-17
train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]


def get_train_name (train_no):
    s=''
    for i in train_list:
        if i['train_no']==train_no:
            s=(i['name'])
        if len(s)>0:
            return s
        else:
            return "invalid Train_no"

def get_trains_for_day(day_of_run):
    l=[]
    for i in train_list:
        l1=i["days_of_run"]
        if day_of_run in l1:
            l.append(i['train_no'])
    if(len(l)>0):
        return l
    else:
        return "Invalid day"

def get_total_fare(train_no,passenger_dict):
    cost=0
    sc=0
    acc=1
    for i in train_list:
        if i['train_no']==train_no:
            acc=i['ac_fare']*passenger_dict["ac"]
            sc=i['sleeper_fare']*passenger_dict["sleeper"]
            cost=acc+sc
    return cost
    
    
print(get_train_name(16453))
print(get_trains_for_day("Mo"))
print(get_total_fare(25627,{"sleeper":10, "ac":10}))


print(get_train_name(25627))
print(get_trains_for_day("Mo"))
print(get_total_fare(22642,{"sleeper":5, "ac":1}))
	
