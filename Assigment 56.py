def max_frequency_word_counter(data):
    data = data.lower()
    string_list = []
    count_list = []
    frequency = 0
    max_length = 0
    word = ""
    str_list = data.split() 
    unique_words = set(str_list) 
      
    for words in unique_words : 
        string_list.append(words)
        count_list.append(str_list.count(words))
        
    for i in range(0,len(count_list)):
        if(count_list[i]>frequency):
            frequency = count_list[i]
            word = string_list[i]
        elif(count_list[i]==frequency):
            frequency = count_list[i]
            if(len(string_list[i])>max_length):
                max_length = len(string_list[i])
                word = string_list[i]

    
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)


#Provide different values for data and test your program.
data="Twinkle Twinkle little star little star"
max_frequency_word_counter(data)
