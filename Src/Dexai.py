import random as rnd

# Reads the data as text from an txt file and parse it 
def Readfile():
    with open("C:/Users/user/Desktop/Dexai/Data/lang.txt", encoding='utf-8') as file:
        lang_data = file.read().split()  # sepeartes it as words
        return lang_data
                 
data = Readfile()  # returns the data as words

# just an function to learn about the dict 
def count_word(data): 
    count = {}
    for i in data:
        count[i] = count.get(i, 0) + 1
    print(count)

count_word(data)
 # end ....

data = Readfile() # main data variable

# this function check the amount words the data contains including duplicate
def word_count(data):
    count = {}
    for tmp in data:
        count[tmp] = count.get(tmp, 0) + 1 # this function checks if the word present if adds one
    return count

count = word_count(data) # storing the data as counted words

# function returns the word probality just calculating the weights 
def count_probability(count, data):
    count_prob = {}
    for key, value in count.items(): # seperating the key and value
        calc = value / len(data) # dividing the value with the total 
        count_prob[key] = calc # reassign the value

    return count_prob

# function checks for repeated pairs in data
def count_pairs(data):
    counted = {}
    lis = []  #  i am stupid as fuck so i am doing this way 
    for tmp in range(len(data)-1): # using the value of the len 
        tup = (data[tmp], data[tmp + 1]) # extracting the first word and next 
        lis.append(tup) # append
    for tmp in lis: # using the list updating the pair as tuple 
        counted[tmp] = counted.get(tmp, 0) +1 # the only method i know bro
    return counted

counted = count_pairs(data) 

# this functions actually creates the weight
def next_word_prob(pair, word):
    result = {}
    pairs = {}
    count = 0
    for key, value in pair.items(): # using the founded pairs 
        first_word = key[0] # for finding the input word
        next_word = key[1] # the next word that was going to be predicted
        if first_word == word: # checking if it is matching
            pairs[key] = value # if matches adding the pair to new dict
            count += value # to calculate the weight
    for key, value in pairs.items(): # we found the weight 
        word = key[1]
        result[word] = value / count
    return result

result = next_word_prob(counted, "hello")

# Using the random library predicting the next word
def predict_next(probalities):
    choices = []
    words = []
    for key, value in probalities.items(): # just extracting the word and key
        choices.append(value)
        words.append(key)
    #passing the word and key as an parameter 
    result = rnd.choices(words, weights = choices)
    print(words, choices)
    return result

print(predict_next(result))
# now it predicts the next word according to the weight 

def text_gen(input, length):
    pass    



