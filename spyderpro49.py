class Person():
    def __init__(self,name,surname,passport,born,phone):
        self.name=name
        self.surname=surname
        self.passport=passport
        self.born=born
        self.phone=phone 
    def get_nameself(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_passport(self):
        return self.passport
    def get_born(self):
        return self.born
    def get_phone(self):
        return self.phone
    def get_info(self):
        info=f"Name: {self.name}\nsurname:{self.surname}\npassport: {self.passport}"
        info+=f"Year of born: {self.born}\nphone nuber: {self.born}"
        return info
class Student(Person):
    def __init__(self,name,surname,passport,university,student_id,subjects):
        super().__init__(self,name,surname,passport)
        self.university=university
        self.student_id=student_id
        self.subjects=[]
    def add_subject(self):
        return [subject for subject in subjects.append()]
    def remove_subject(self):
        if subject in subjects[]:
            return f"there is not this subject"
        else:
            subjects.remove(self.subject)
            return f"{self.subject} removed, {subjects[:]}"
class Subject():
    def __init__(self,name,book,closesubject):
        self.name=name
        self.book=book
        self.closesubject=closesubject
        self.duration=45
    def get_subject(self):
        info=f"Name of subject: {self.name}\n Name of book:{self.book}"
        info+=f"Close subject: {self.closesubject}"
class Workers(Person):
    def __init__(self,name,surname,job,passport,working_hour):
        super().__init__(self,name,surname,passport)
        self.job=job
        self.working_hour=8
    def get_job(self):
        return self.job
    def get_working_hour(self):
        return self.working_hour
    
class professors(Person):
    def __init__(self,name,surname,sphere,passport, university):
        super().__init__(self,name,surname,passport)
        self.sphere=sphere
    def get_sphere(self):
        return self.sphere

    