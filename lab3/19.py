#PYTHON Inheritance
# Exercise 1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Exercise 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
