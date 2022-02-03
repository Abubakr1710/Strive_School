from f1 import Person

class Teacher(Person):
    def __init__(self, fname, lname,tech_id):
        super().__init__(fname, lname)
        self.tech_id = tech_id

    def printname(self):
        print(self.firstname, self.lastname, self.tech_id)

x = Teacher("Robert","Dale",1717)
x.printname()