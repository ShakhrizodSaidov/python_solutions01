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
    return titled_names

def capitalizer2(names):
    titled_names=[]
    for i in range(len(names)):
        name=names[i].title()
        titled_names.append(name)
    return titled_names

names = ['ali', 'vali', 'hasan', 'husan']
print(capitalizer(names[:]))
print(capitalizer2(names[:]))


