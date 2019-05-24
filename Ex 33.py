def human_pyramid(no_of_people):
    n=0
    for i in range(1,no_of_people+1,2):
        n+=i*50
    return n

def find_maximum_people(max_weight):
    no_of_people=1
    weight=0
    max=1
    while(max_weight>=weight):
        weight=human_pyramid(no_of_people)
        if(weight<=max_weight):
            max=no_of_people
        no_of_people+=2
    return max
    
    print(find_maximum_people(800))
