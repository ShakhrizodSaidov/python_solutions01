# with open('C:/Users/Shahrizod/Documents/GitHub/pi.txt') as file:
#     pi=file.read()
#     pi=pi.rstrip('')
#     pi=pi.replace('\n','' )
#     pi=float(pi)
# # filename = 'data/talabalar.txt'
# # with open(filename) as file:
# #     for line in file:
# #         print(line)
# # talabalar = [talaba.rstrip() for talaba in talabalar]
# # print(talabalar)
name="Shahrizod"
surname="Saidov"
was_born=1998
language='english'

filename='newfile.txt'
with open(filename,'a') as file:
    file.write(name)
    file.write(surname)
    file.write(str(was_born))
    file.write(language)
    
yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)  
    print(f"Siz {2021-yosh} yilda tug'ilgansiz")  
except:
    print("Butun son kiritmadingiz")

print("Dastur Tugadi!")