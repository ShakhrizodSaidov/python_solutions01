print("We will create dictionary about your friends.")
friends={}
i=1
while True:
    friend=input(f"Please, enter a name of your {i}-friend: ")
    age=int(input(f"Please enter you {friend}'s age: "))
    friends[friend]=age
    msg=input("do you wana add again?(yes/no)")
    i+=1
    if msg=='yes':
        continue
    else:
        break
for friend, age in friends.items():
    print(f"{friend.title()} is {age} years old")
print(friends)