def check_double(number):
    s=number*2
    t1=[int(x) for x in str(number)]
    t2=[int(x) for x in str(s)]
    t1.sort()
    t2.sort()
    if(t1==t2):
        return True
    else:
        return False
print(check_double(125874))
