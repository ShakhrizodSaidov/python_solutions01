menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")