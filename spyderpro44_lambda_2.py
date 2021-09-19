# from math import sqrt

# nums = list(range(11)) # 0 dan 10 gacha numbers_list ro'yxati
# square_root = list(map(sqrt,nums))


# numbers_list = list(range(11)) 

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,numbers_list)))


# def numbers(x):
#     return x**2
# kv=[]
# for son in  numbers_list:
#     son=numbers(son)
#     kv.append(son)
# print(kv)

# print(list(map(lambda x:x**2,numbers_list)))
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)


# names = ['hasan','husan','olim','umid']
# print(list(map(lambda x:x.upper(),names)))
# import random as r

# sonlar = r.sample(range(100),10) 

# def juftmi(x):
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)
from random import sample
from math import sqrt,floor
x=list(range(0,1001))
y=sample(x,k=10)
print(y)
print(list(((map(lambda x:sqrt(x),y)))))
print(list(filter(lambda x:(x%2!=0),y)))
print(list(filter(lambda x:(x%2==0),y)))

