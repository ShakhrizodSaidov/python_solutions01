# =============================================================================
# Take a list of texts and write a 
# function that converts the first letter of each 
# text in the list to uppercase.
# =============================================================================
def capitalizer(names):
    titled_names=[]
    while names:
        name=names.pop()
        name=name.title()
        titled_names.append(name)
        titled_names.reverse()
    return titled_names

def capitalizer2(names):
    titled_names=[]
    for i in range(len(names)):
        name=names[i].title()
        titled_names.append(name)
    return titled_names

def marker(names):
    marked_students={}
    for i in range(len(names)):
        name=names[i].title()
        mark=int(input(f"Enter a mark to {names[i].title()}: "))
        marked_students[name]=mark
    return marked_students

names = ['ali', 'vali', 'hasan', 'husan']
print(marker(names))
print(capitalizer(names[:]))
print(capitalizer2(names[:]))


