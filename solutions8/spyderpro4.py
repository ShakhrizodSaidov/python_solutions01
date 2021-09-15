
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', \
               'piyoz','kartoshka', 'olma',\
                'banan', 'uzum', 'qovun']  
basket=[]
for i in range(5):
    basket.append(input(f"{i+1} chi mevaning nomini kiriting: "))
    if basket[i] in mahsulotlar:
        print(f"we have {basket[i]}")
    else: print("we dont have ")
        