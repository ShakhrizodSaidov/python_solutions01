print("Lets create list of your close friends")

friends=[]
i=1
while True:
    friend=input(f"please enter your {i}-friend: ").lower()
    friends.append(friend)
    yes_no=input("do you wanna add again? ")
    if yes_no!='yes':
        break
    else:
        i+=1
print(f"Your close friends ara:")
for friend in friends:
    print(friend.title())
    

    
