question ="This is root calculator of entered number.\n"
question += "Enter a positive number"
question += "(type 'exit' to stop operation): "
value=None
while True:
    value = input(question)
    if value=='exit':
        break
    elif int(value)<0:
        continue
    else:
        value=int(value)
        root = float(value)**(0.5)
        print(f"The root of {value} equalis equal {root}")
print("operation is ended")