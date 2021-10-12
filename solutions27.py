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
##############
books=[]
flag=True
while flag:
    book=input("Enter a book(to quit type 'quit'):")
    if book=='quit':
        print('operation is ended..')
        flag=False
    else:
        books.append(book)
        print(f"Your books:{set(books)}" )
print(f'entered books: {set(books)}')
##############
