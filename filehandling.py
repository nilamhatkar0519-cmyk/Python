import os

# Create and write data
file = open("student.txt", "w")

file.write("Name : Nilam Hatkar\n")
file.write("Roll No : 70\n")
file.write("Course : AJP\n")
file.close()


# 1. Open the file in read mode
file = open("student.txt", "r")

print("----- Student Details -----")
print(file.read())
file.close()


# 2. Append data
file = open("student.txt", "a")

file.write("\nName : Sahil Patil\n")
file.write("Roll No : 35\n")
file.write("Course : AJP\n")
file.close()

# 3. Read the file after appending
file = open("student.txt", "r")

print("----- After Appending -----")
print(file.read())
file.close()


# 4. wb 
file = open("student.txt", "wb")
print(file.write(b"Hello student!!"))
file.close() 

# 5. rb 
file = open("student.txt", "rb")
print(file.read())
file.close() 

# 6.ab 
file = file = open("student.txt", "ab")
data = file.write(b"How are you all ??")
file.close()



### reading file ###
# 1. read 
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# 2. readline 
file = open("student.txt", "r")
print(file.readline())
file.close()

# 3. readlines 
file = open("student.txt", "r")
print(file.readlines())
file.close()

# 4.tell()

file = open("student.txt", "r")
print(file.tell())

data = file.read(5)
print(data)
print(file.tell())
file.close()

# 5. seek()

file = open("student.txt", "r")
print(file.seek(3))

file.seek(0)
print(file.read())
file.close()
