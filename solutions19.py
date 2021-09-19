countries = {
    "uzbekistan": 'tashkent',
    'aqsh': 'washington d.c.',
    'russia': 'moscow',
    'tajikistan': 'dushanbe',
    "Kyrgyzstan": 'Bishkek',
    'kazog \' iston ':' nursulton ',
    'malaysia': 'kuala-lumpur',
    'singapur': 'sungapur',
    'italia': 'rim'}
# if user in countries.keys():
#     if user=="aqsh":
#         print(f"{user.upper()}ning poytaxti {countries[user].title()}")
#     else:
#         print(f"{user.upper()}ning poytaxti {countries[user].title()}")
# else:
#     print(f"sorry, we dont have info about {user.title()} country")
        
    
country = input ("Which country's capital do you want to know?:").lower ()
capital = countries.get (country)
if capital == None:
    print ('Sorry, we have no information about this')
else:
    print (f"{capital.title ()} is the capital of {country.upper ()}")