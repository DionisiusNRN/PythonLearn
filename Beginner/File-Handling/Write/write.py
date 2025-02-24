# # Append (will append to the end of the file)
# f = open("demofile2.txt", "a")
# f.write("Adding some content here...")
# f.close() # must be closed, so the file will update

# f = open("demofile2.txt", "r") # read
# print(f.read())



# # Write (will overwrite any existing content)
# f = open("demofile3.txt", "w")
# f.write("I Overrite the demofile3.txt file")
# f.close()

# f = open("demofile3.txt", "r") # read
# print(f.read())



# CREATE A NEW FILE
f = open("demofile4.txt", "x")
f = open("demofile5.txt", "w")
f = open("demofile6.txt", "a")
