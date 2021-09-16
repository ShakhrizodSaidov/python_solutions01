
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', \
#                'piyoz','kartoshka', 'olma',\
#                 'banan', 'uzum', 'qovun']  
# basket=[]
# for i in range(5):
#     basket.append(input(f"{i+1} chi mevaning nomini kiriting: "))
#     if basket[i] in mahsulotlar:
#         print(f"we have {basket[i]}")
#     else: print("we dont have ")
        
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    