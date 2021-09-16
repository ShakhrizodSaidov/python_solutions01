davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
# user=input("what country do you want to travel: ").lower()
# if user in davlatlar.keys():
#     if user=="aqsh":
#         print(f"{user.upper()}ning poytaxti {davlatlar[user].title()}")
#     else:
#         print(f"{user.upper()}ning poytaxti {davlatlar[user].title()}")
# else:
#     print(f"sorry, we dont have info about {user.title()} country")
        
    
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")