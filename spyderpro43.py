def mark_giver(names):
   marked_students={}
   while names:
       student=names.pop()
       mark=int(input(f"give a mark to {student}: "))
       marked_students[student]=mark
   return marked_students

names=['Shahrizod','Olim','Xurshid','Vova']  
print(mark_giver(names[:]))      