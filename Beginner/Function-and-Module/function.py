# def my_function():
#     print("hello from my_function")

# my_function() # calling a function


# def my_function(fname): #arguments
#     print("Helo " + fname + ", from my_function")

# my_function("Jupri")
# my_function("bambank")


# def my_function(fname, lname): #number of arguments
#     print(fname + " " + lname)

# my_function("Jupri", "Junior") # must be number of arguments


# def my_function(*kids): #arbitrary arguments (you dont know the number of arguments)
#     print("the youngest kids is " + kids[2])

# my_function("Jupri", "bambank", "michael")


# def my_function(child3, child2, child1): #keyword arguments
#     print("the youngest kids is " + child2)

# my_function(child1 = "Jupri", child2 = "bambank", child3 = "michael")


# def my_function(**kid): #arbitrary keyword arguments, **kwargs
#     print("his last name is " + kid["lname"])

# my_function(fname = "Jupri", lname = "michael")


# def my_function(country = "German"): #default parameter value
#     print("i am from " + country)

# my_function("Indonesia")
# my_function()
# my_function("China")


# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "orange"]
# my_function(fruits) # passing list as argument


# def my_function(x):
#     return 5 * x #return

# print(my_function(3))
# print(my_function(5))


# def my_function(): #in case you have empty content in your function
#     pass # use pass for not getting an error message


# def my_function(x, /):
#     print(x)

# my_function(3) # positional-only argument (safety for API/public methods)


# def my_function(*, x):
#     print(x)

# my_function(x = 3) # keyword-only argument (simple)


# # Combine Positional-Only and Keyword-Only
# def my_function(a, b, /, *, c, d):
#     print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)


# # Recursion
# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1) # semacam looping function
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results:")
# tri_recursion(6)


# # penjelasan recursion
# dari ini: result = k + tri_recursion(k - 1)
# hasilnya jadi begini:
# 6 + tri_recursion(6 - 1)
# 6 + (5 + tri_recursion(5 - 1))
# 6 + (5 + (4 + tri_recursion(4 - 1)))
# dan seterusnya...

# hasilnya
# 6 + (5 + (4 + (3 + (2 + (1 + (0))))))
# "menjumlahkan dari kurung yang paling dalam"
