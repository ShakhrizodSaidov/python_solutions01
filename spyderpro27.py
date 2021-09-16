# flag=True
# while flag:
while True:
    age_msg=input("Plese,enter your age:")
    if age_msg=='exit' or age_msg=='quit':
        # flag=False
        break
    else:
        age=int(age_msg)
        if age<7:
            ticket=2000 
            print(ticket)
        elif age>=7 and age<18:
            ticket=3000 
            print(ticket)            
        elif age>=18 and age<=65:
            ticket=10000
            print(ticket)
        elif age>65:
             print("Ticket is free for you")
print("Operation is ended")
          