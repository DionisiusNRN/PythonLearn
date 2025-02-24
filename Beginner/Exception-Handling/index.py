# try: # test a block of code for errors
#     print(x)
# except: # lets you handle errors
#     print("something else went wrong")


# print(x) # usual error


# try:
#     print(x)
# except NameError: # for NameError
#     print("variable x not found")
# except: # for other errors
#     print("something else went wrong")


# try:
#     print("Hello")
# except:
#     print("something else went wrong")
# else: # executed if no errors
#     print("Nothing went wrong")



# try:
#     print("Hello")
# except:
#     print("something else went wrong")
# else: # executed if no errors
#     print("Nothing went wrong")



# try:
#     print(x)
# except:
#     print("something else went wrong")
# finally: # executed whenever "try" is error or not
#     print("the 'try except' is finished")



# x = -1
# if x < 0:
#     raise Exception("Sorry, no number below zero") # usual error + Exception error



x = "Hello"
if not type(x) is int:
    raise TypeError("Only integer are allowed") # usual error + TypeError message
