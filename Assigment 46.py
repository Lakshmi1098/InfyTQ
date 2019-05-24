
def nearest_palindrome(number):
    f=True
    while(f):
        number+=1
        s=str(number)
        if(s==s[-1::-1]):
            f= False
    return number

number=12300
print(nearest_palindrome(number))
