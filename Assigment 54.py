def check_anagram(data1,data2):
    data1=data1.lower()
    data2=data2.lower()
    l=[]
    c=0
    if(len(data1)==len(data2)):
        for i in range(len(data1)):
            for j in range(len(data2)):
                if(data1[i]==data2[j] and i!=j and not(j in l)):
                    l.append(j)
                    c=c+1
                    break
    if(c==len(data2)):
        return True
    else:
        return False
print(check_anagram("aab","bca"))
