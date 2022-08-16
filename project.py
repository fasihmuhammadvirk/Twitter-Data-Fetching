
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    
    for i in s:
        if i in punctuation_chars:
            
            s = s.replace(i,'')       
    return s 


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            


# functions 

def get_pos(x):
    
    new_string = strip_punctuation(x)
    occurance = 0
    for word in new_string.split():
        if word.lower() in positive_words:
            occurance += 1 
    return occurance
            
            
def get_neg(x):
    
    new_string = strip_punctuation(x)
    occurance = 0
    for word in new_string.split():
        if word.lower() in negative_words:
            occurance += 1 
    return occurance

            
#main project 



with open("resulting_data.csv" , 'w') as p:
    
    p.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    p.write('\n')
    
    with open("project_twitter_data.csv") as ptd_f:
        lines = ptd_f.readlines()

        header = lines[0]
        tweets = header.strip().split(',')
        print(tweets)

        for row in lines[1:]:

            vals = row.strip().split(',')


            if vals[2] != '\n':
                
                
                number_of_retweets = vals[1]
                number_of_replies = vals [2]
                positive_score = get_pos(vals[0])
                negative_score = get_neg(vals[0])
                net_score =  int(positive_score) - (negative_score)
                
                row_string = "{}, {}, {}, {}, {}".format(
                    
                    number_of_retweets,
                    number_of_replies,
                    positive_score,
                    negative_score,
                    net_score
                    
                )
                
                p.write(row_string)
                p.write('\n')
               
                

            


