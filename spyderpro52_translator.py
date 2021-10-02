from googletrans import Translator
msg1=input('Your domain: ')
msg2=input('foreign domain: ')
msg0=f"Please, enter anything to translate '{msg1}_{msg2}'(press 'q' to quit, press 'e' to change foreign domain): "
out0=Translator().translate(msg0,dest=msg1, src=msg2)
print(out0.text)
while True:
    msg=input()
    if msg=='q':
        break
    elif msg=='e':
        msg2=input('enter foreign language domain: ')
        msg=input()
        out=Translator().translate(msg,dest=msg2,src=msg1)
        print(out.text)
      
    else:
        out=Translator().translate(msg,dest=msg2,src=msg1)
        print(out.text)