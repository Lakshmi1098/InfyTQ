#PF-Assgn-30

def encode(message):
    st=""
    c=0 
    s=message[0]
    for i in range(0,len(message)):
        if(message[i]==s):
            c+=1 
        else:
            st+=str(c)+s
            s=message[i]
            c=1
        if(int(i)==len(message)-1):
            st+=str(c)+s
    return st
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
