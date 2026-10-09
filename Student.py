class Student:
    def __init__(self,name,id,grade):
        self.name = name
        self.id = id
        self.grade = grade
    
    
    def details(self):
        print(f"{self.name} has grade: {self.grade} and has student id: {self.id}")
    def has_passed(self):
        if self.grade >= 50:
            return True
        else:
            return False    
