from uzwords import words
from random import choice, randint,sample
word=choice(words).upper()
print(f"I have thought {len(word)} rom number, can you guess??")
word_list=list(word)
guessing_word=[]
for i in range(len(word)):
    guessing_word.append('-')
print(''.join(guessing_word),end='')
flag=True
letter_list=[]
i=1
while ''.join(guessing_word)!=word:
    letter=input('\nEnter a letter: ').upper()
    letter_list.append(letter)
    print(f"Letters you have entered: {set(letter_list)}")
    if letter in word_list:
        print(f"{letter} letter is true")
        guessing_word[word_list.index(letter)]=letter 
        print(''.join(guessing_word),end='')
    else:
        print("No such letter!")
        print(''.join(guessing_word),end='')
        i+=1
print(f"Finally you have found with {i} guesses!!")
