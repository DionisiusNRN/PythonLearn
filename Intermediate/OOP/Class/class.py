# # SIMPLEST EXAMPLE
# class MyClass: # create a class
#     x = 5

# p1 = MyClass()
# print(p1.x)



# # __init__()
# class Person:
#     def __init__(self, name, age): # constructor function
#         self.name = name
#         self.age = age

# p1 = Person("John", 35)
# print(p1.name)
# print(p1.age)



# # __str__()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self): # control what should be returned when the class object is represented as a string
#         return f"{self.name}({self.age})"

# p1 = Person("John", 35)
# print(p1)



# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 35)
p1.myfunc()

# # modify object properties
# p1.name = "Rangga" # change value
# del p1.age # delete object properties
# del p1 # delete object

