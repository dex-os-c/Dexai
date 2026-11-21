def Readfile():
    with open("Data/lang.txt", encoding='utf-8') as file:
        lang_data = file.read().split()
        print(lang_data)
            
            
            
Readfile()