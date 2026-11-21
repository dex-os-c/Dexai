def Readfile():
    with open("Data/lang.txt", encoding='utf-8') as file:
        lang_data = file.read().split()
        return lang_data
            
                      
data = Readfile()
print(data)