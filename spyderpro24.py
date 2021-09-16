countries={
     'uzbekistan':{'capital':'Tashkent',
                   'money':'sum',
                   'nationality':'uzbek',
                   'independent year':1991,
                   'area': 448,
                   'population':34                   
                     },  
         'russia':{'capital':'moscow',
                   'money':'ruble',
                   'nationality':'russian',
                   'independent year':1991,
                   'area': 1730,
                   'population':144.4                   
                     },
         'usa':{'capital':'washington d.c',
                   'money':'dollar',
                   'nationality':'american',
                   'independent year':1776,
                   'area': 9834,
                   'population':328.2                   
                     },   
         'china':{'capital':'pekin',
                   'money':'renminbi',
                   'nationality':'chinesse',
                   'independent year':1912,
                   'area': 9597,
                   'population':1398                   
                     }   
    }
country=input("Please, enter a country: ").lower()
print("\n")
if country in countries:
    print(f"Capital is {countries[country]['capital'].title()}\n"
          f"money:{countries[country]['money'].lower()}\n"
          f"nationality: {countries[country]['nationality']}\n"
          f"indapendent year: {countries[country]['independent year']}\n"
          f"area: {countries[country]['area']}\n"
          f"population: {countries[country]['population']}\n")

else:print("We dont have information about this country(error).")
# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")
        