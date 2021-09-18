orders = ['apple','pineapple','grapes','melon']
products = {'apple':20000,
               'pineapple':25000,
               'watermelon':18000,
               'grapes':22000}
while orders:
    product=orders.pop()
    if product in products.keys():
        print(f"we have {product}, its price is:{products[product]}")
    else:
        print(f"we dont have {product}")