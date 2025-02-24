f = open("demofile.txt", "r") # "r" is default value


# print(f.read()) # read whole file

# print(f.read(5)) # read juts 5 character at the beginning

# print(f.readline()) # read just one line

# # read two lines
# print(f.readline())
# print(f.readline())

# for x in f: # read the whole file line by line
#     print(x)

print(f.readline())
f.close() # close the file
