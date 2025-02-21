# #use a module
# import mymodule as mx # re-naming a module
from mymodule import person1 # from mymodule ONLY import person1

# # 1
# mymodule.greeting("Jupri")


# # 2
# a = mymodule.person1["age"]
# print(a)


# x = dir(mx) # to show all the functions name
# print(x)


# if you are "from" when import, do not use the module name when referring
print(person1["age"])
