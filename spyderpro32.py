print("We gonna create a list of products for market")
products={}
i=1
while True :
        product=input(f"Please enter {i}-product's name':")
        value=int(input(f"Please enter {product}'s price':"))
        products[product]=value
        i+=1
        msg=input("Do you want again?(yes/no)")
        if msg!='yes':
            break
print(products)