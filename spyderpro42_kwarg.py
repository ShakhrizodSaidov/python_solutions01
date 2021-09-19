def students(name,surname,**info):
    info['name']=name    
    info['surname']=surname 
    return info

student1=students('Shahrizod','Saidov',subject='math', mark=5)
student2=students('Xurshid','Abdurazaqov', subject='pysics', mark=4)