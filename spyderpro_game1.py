from random import choice 
print("Let's play a game to find a thinked number")
x=choice(range(1,11))
print("I thougt a number in range 1 to 10, can you guess??")
y=int(input(">>>"))
flag1=True
i=1
while flag1:
    if y<x:
        y=int(input("False,number is _greater_ than a number I thought, try again: "))
        i+=1
    elif y>x:
        y=int(input("False,number is _smaller_ than a number I thought, try again: "))
        i+=1
    else:
        print(f"Great! You found it!(guess number is {i})\n")
        flag1=False
print("Its is my turn, think a number and I'll guess to find it ;)")
flag2=True
low=1
high=10
j=1
while flag2:
    middle = low + (high - low) // 2
    msg1=input(f"The number you have gussed is ' {middle}? ' \n(type 'T' else, if greater type (+) else (-))): ")
    if msg1=='T':
        flag2=False
        print(f"Number of my guesses is {j}")
    elif msg1=='+':
        low = middle + 1
        j+=1
    elif msg1=='-':
        high = middle - 1
        j+=1
if i<j:
    print('You win!')
elif i>j:
    print('You lost!')
else:
    print(f"It seems we both are clever! ;)")       
        

