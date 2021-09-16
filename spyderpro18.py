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
print("davlatlar quyidagilar:")
for key in sorted(davlatlar.keys()):
    print(key.title())
print("\n")
print("shaharlar quyidagilar:")
for value in sorted(davlatlar.values()):
    print(value.title())
user=input("Qaysi davlat poytaxtini bilishni hohlaysiz?:\n")
user=user.lower()
if user in davlatlar.keys():
    print(f"{davlatlar[user].title()}")
else:
    print(f"Bizda {user.title()} davlatining ma`lumoti yo`q")
    