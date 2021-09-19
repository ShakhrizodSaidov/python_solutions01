def multiplication(numbers):
    result=1
    for i in numbers:
        result=i*result
    return result 

nums=[]
flag=True
i=1
while flag:
    num=input(f'enter {i}-number(to stop, type "stop"): ')
    if num!="stop":
        i=i+1
        num=int(num)
        nums.append(num) 
    else: flag=False

print(f"{multiplication(nums[:])}\n")

def multipl(*numbers):
    result=1
    for i in numbers:
        result=i*result
    return result 
print(multipl(1,2,3,4,5,6,7,8,9))
