from random import sample
def isprime(x):
    if x%2==0 or x<2: return False 
    if x==2 or x==3: return True 
    for i in range(3,x,2):
        if x%i==0: return False 
    return True
nums=sample(list(range(1,100)),20)
print(list(filter(isprime,nums)))
