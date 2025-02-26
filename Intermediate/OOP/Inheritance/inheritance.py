class Person: # parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


class Student(Person): # child class
    def __init__(self, fname, lname, year): # add parameter
        super().__init__(fname, lname)
        self.graduationyear = year # add properties (make it object)

    # def __init__(self, fname, lname):
    #     super().__init__(fname, lname) # keep the inherit all the methods and properties from its parent
    #     self.graduationyear = 2020 # add properties

    # def __init__(self, fname, lname):
        # #add properties etc. # this is overrides the inheritance of the parent's __init__() function.
        # Person.__init__(self, fname, lname) # keep the inheritance of the parent's

    def welcome(self): # add methods
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Tyson", 2020)
x.welcome()
