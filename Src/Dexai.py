def Readfile():
    with open("C:/Users/user/Desktop/Dexai/Data/lang.txt", encoding='utf-8') as file:
        lang_data = file.read().split()
        return lang_data
                 
data = Readfile()

def count_word(data):
    count = {}
    for i in data:
        count[i] = count.get(i, 0) + 1
    print(count)

count_word(data)