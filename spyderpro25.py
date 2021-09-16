print('this program can square your value!')
ques="Please enter any number"
ques+="(if you dont want, type 'exit'): "
value=None
while value!='exit':
    value=input(ques)
    if value!='exit':
        print(float(value)**2)
print('the end....')