# =============================================================================
# Foydalanuvchidan aylaning radiusini qabul qilib olib,
#  uning radiusini, diametrini, perimetri va yuzini 
#  lug'at ko'rinishida qaytaruvchi funksiya yozing
# =============================================================================
def radius(r):
    d=2*r
    p=2*3.14*r
    s=3.14*(r**2)
    diction={
        'radius':r,
        'diameter':d,
        'perimeter':p,
        'surface':s
        }
    return diction
n=int(input("enter radius: "))
m=radius(n)
print(m)
