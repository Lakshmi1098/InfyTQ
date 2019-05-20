#PF-Assgn-33

def find_common_characters(msg1,msg2):
    st=""
    count=0
    for i in range(0,len(msg1)):
        for j in range(0,len(msg2)):
            if(msg1[i]!=" "and msg1[i]==msg2[j]):
                if(msg1[i] in st):
                    continue
                else:
                    st+=msg1[i]
                    count=1 
    if(count==0):
        return -1
        
    else:
        return st
    

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)

print(*common_characters)
