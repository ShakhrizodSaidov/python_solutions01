age=int(input("Please, enter your age: "))
if age<4 or age>60:
    narh=0
elif age<18:
    narh=10000
elif age>=18:
    narh=20000
if narh==0:
    print("Ticket is free for you")
else:print(f"Price of ticket for you is {narh}")