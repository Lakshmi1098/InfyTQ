a=list(map(int,input().split()))
a.sort(reverse=True)
for i in a:
    print(i,end="")

    
    
    ANOTHER METHOD:
        a=[23,34,55]
        a.sor(reverse=True)
        res=[str(i) for i in a]
        r=int("".join(res))
        print(res)
