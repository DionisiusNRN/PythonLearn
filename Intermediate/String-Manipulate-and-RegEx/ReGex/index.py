import re

txt = "The rain in Spain"


# x = re.search("^The.*Spain$", txt) # Search the string to see if it starts with "The" and ends with "Spain"
# print(x)

# x1 = re.findall("ai", txt) # print a list of all matches
# x2 = re.findall("Portugal", txt) # Return an empty list if no match was found
# print(x1)
# print(x2)

# x = re.search("\s", txt) # Search for the first white-space character in the string
# print("The first white-space character is located in position:", x.start())
# x = re.search("Portugal", txt) #
# print(x)

# x = re.split("\s", txt) # split at each white-space character
# print(x)
# x = re.split("\s", txt, 1) # Split the string only at the first occurrence
# print(x)

# x = re.sub("\s", "9", txt) # Replace every white-space character with the number 9
# print(x)
# x = re.sub("\s", "9", txt, 2) # Replace the first 2 occurrences
# print(x)

# x = re.search("ai", txt) #
# print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
