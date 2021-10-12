python_words = {
    'integer':'Butun son',
    'float': "O'nlik son",
    'boolean':"Mantiqiy qiymat",
    'for':"Biror amalni qayta-qayta bajarish tsikli",
    'if':'Shartlarni tekshirish operatori'}
for item in sorted(python_words):
    print(f"{item.capitalize()}-{python_words[item]}")
#for keys,values in sorted(python_words.items()):
#    print(f"{keys.title()}-{values.capitalize()}")
   
