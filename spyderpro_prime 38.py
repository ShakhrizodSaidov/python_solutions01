def prime(a,b):
    prime_nums=[]
    for num in range(a, b + 1):
       if True:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               prime_nums.append(num)
    print(prime_nums)
prime(2,7)