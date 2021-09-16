print('this program can square your value!')
ques="Please enter any number"
ques+="(if you dont want, type 'exit'): "
flag=True
while flag:
    value=input(ques)
    if value=='exit':
        flag=False
    else:
        print(float(value)**2)
print('the end....')