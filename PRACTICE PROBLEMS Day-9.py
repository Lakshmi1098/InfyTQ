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


