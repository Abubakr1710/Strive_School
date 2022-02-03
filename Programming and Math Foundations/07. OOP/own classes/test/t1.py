class Person:
  def __init__(self, fname, lname, birth_year):
    self.firstname = fname
    self.lastname = lname
    self.year = birth_year

  def __str__(self):
    return f'First Name: {self.firstname}\nLast Name: {self.lastname}\nBirth year: {self.year}'