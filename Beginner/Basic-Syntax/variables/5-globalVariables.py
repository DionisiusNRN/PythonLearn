# x = "awesome"
# def myfunc():
#     print("Python is " + x)

# myfunc() # Python is awesome!


# # WHAT IF?
# x = "awesome"
# def myfunc():
#     x = "great"
#     print("World are " + x)

# myfunc() # World are great!
# print("World are " + x) # World are awesome!


# THE GLOBAL KEYWORDS
# def myfunc():
#     global x
#     x = "globals"

# myfunc() # for declarations of "global" variables
# print("This is " + x) # call the "global"


x = "outside" # replace by global variable
def myfunc():
    global x
    x = "globals"

myfunc() # for declarations of "global" variables
print("This is " + x) # call the "global"
