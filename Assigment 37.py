child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    sum=0
    for i in range(0,len(chocolates_received)):
        sum+=chocolates_received[i]
    return sum

def reward_child(child_id_rewarded,extra_chocolates):
    c=0
    if(extra_chocolates<1):
        print("Extra chocolates is less than 1")
    else:
        for i in range(0,len(child_id)):
            if(child_id[i]==child_id_rewarded):
                chocolates_received[i]+=extra_chocolates
                c=1
        if(c==1):
            print(chocolates_received)
        else:
            print("Child id is invalid")
print(calculate_total_chocolates())
reward_child(20,2)
