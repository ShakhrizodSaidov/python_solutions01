message="Please, enter your favourite books: "
flag=True
books=[]
while flag:
    print('to stop type "stop"',end='')
    book=input(message)
    print('\n')
    if book=='stop':
        flag=False
    else:
        books.append(book.title())
if set(books)=={''}:
    print("no book entered")
else:
    print(f"List of your books is {set(books)}")
print("Operation was ended")