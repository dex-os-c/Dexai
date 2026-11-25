import random as rnd


def Readfile():
    with open("C:/Users/user/Desktop/Dexai/Data/lang.txt", encoding='utf-8') as file:
        lang_data = file.read().split()
        return lang_data
<<<<<<< HEAD
                 
data = Readfile()

def count_word(data):
    count = {}
    for i in data:
        count[i] = count.get(i, 0) + 1
    print(count)

count_word(data)
=======


data = Readfile()

def word_count(data):
    count = {}
    for tmp in data:
        count[tmp] = count.get(tmp, 0) + 1
    return count

count = word_count(data)

def count_probability(count, data):
    count_prob = {}
    for key, value in count.items():
        calc = value / len(data)
        count_prob[key] = calc

    return count_prob

def count_pairs(data):
    counted = {}
    lis = []
    for tmp in range(len(data)-1):
        tup = (data[tmp], data[tmp + 1])
        lis.append(tup)
    for tmp in lis:
        counted[tmp] = counted.get(tmp, 0) +1
    return counted

counted = count_pairs(data)

def next_word_prob(pair, word):
    result = {}
    pairs = {}
    count = 0
    for key, value in pair.items():
        first_word = key[0]
        next_word = key[1]
        if first_word == word:
            pairs[key] = value
            count += value
    for key, value in pairs.items():
        word = key[1]
        result[word] = value / count
    return result

result = next_word_prob(counted, "hello")

def predict_next(probalities):
    choices = []
    words = []
    for key, value in probalities.items():
        choices.append(value)
        words.append(key)

    result = rnd.choices(words, weights = choices)
    print(words, choices)
    return result

print(predict_next(result))


def text_gen(input, length):
    



