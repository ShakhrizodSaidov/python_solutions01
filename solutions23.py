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
# countries=[];
# for country in davlatlar:
#     if country=='usa':
#         countries.append(country.upper())
#     else:
#         countries.append(country.title())
       
for country,values in countries.items():
    if country=='usa':
        country="USA"
    else:
        country=country.title()
    print(f"{country}\n Capital is {values['capital'].title()}\n"
          f"money:{values['money'].lower()}\n"
          f"nationality: {values['nationality']}\n"
          f"indapendent year: {values['independent year']}\n"
          f"area: {values['area']}\n"
          f"population: {values['population']}\n")
    
