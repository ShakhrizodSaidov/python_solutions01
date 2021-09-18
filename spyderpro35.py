# =============================================================================
# Foydanaluvchidan ismi, familiyasi,
# tug'ilgan yili, tug'ilgan joyi, email manzili va telefon
# raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi 
# funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
# Ba'zi argumentlarni 
# kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# =============================================================================
def pers_info(name,surname,born,place,email=None,phone=None):
    person={
        'name':name,
        'surname':surname,
        'born':born,
        'place':place,
        'email':email,  
        'phone':phone
        }
    return person
people=[]
while True:
    print("Enter fill the form below:")
    name=input("name: ").title()
    surname=input("surname: ").title()
    born=int(input("When_born: "))
    place=input("where_born: ")
    email=input("email(may type 'no'): ")
    if email=='no':
        email='no info:('
    phone=(input("phone(if no type 'no'): "))
    if phone=='no':
        phone='no info:('
    person=pers_info(name, surname, born, place,email,phone)
    people.append(person)        
    msg=input('do you wanna enter again?(yes/no)')
    if msg=='no':
        break
print(people)
print("Operation is ended successfully;)")