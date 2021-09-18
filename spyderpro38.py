def fibonacci(n):
    sonlar = []
    for i in range(n):
        if i==0 or i==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[i-1]+sonlar[i-2])
    return sonlar

print(fibonacci(10))
            
        