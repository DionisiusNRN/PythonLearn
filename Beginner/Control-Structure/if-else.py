# a = 10
# b = 200
# if b > a:
#     print("b greater than a") # Indentation


# a = 33
# b = 33
# if a > b:
#     print("a is greater than b")
# elif b == a: # elif is another condition
#     print("a and b are equal")


# a = 33
# b = 200
# if a > b:
#     print("a is greater than b")
# elif b == a:
#     print("a and b are equal")
# else: # else is another condition except if or elif
#     print("b is greater than a")


# # SHORT HAND
# a = 10
# b = 10
# if a < b: print("a is less than b") # if
# print(a) if a > b else print(b) # if...else
# print(a) if a > b else print("=") if a == b else print(b) # if else 3 condition


# a = 200
# b = 33
# c = 100

# # And (must true either of them)
# if a > b and b < c:
#     print("Both are true")

# # Or (must true one or both of them)
# if a < b or c > b:
#     print("At least one is true")

# # Not
# if not a < b:
#     print("b is NOT greater than a")

# # Nested if
# if a > 10:
#     print("a is above 10")
#     if a < 20:
#         print("a is also above 20")
#     else:
#         print("a is not above 20")


# The pass Statement
a = 33
b = 200
if a > b:
    pass # if condition not met, do nothing
