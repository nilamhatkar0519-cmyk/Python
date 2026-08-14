import os 

# 1.create directory 
os.mkdir("example")
print("directory successfully created ") 

# 2. check directory exists or not 
if os.path.exists("student"):
    print("directory exists")
else:
    print("directory doesn't exists")
    

# 3. get current working directory 
print(os.getcwd())

# 4. change directory 
os.chdir("students")
print(os.getcwd())

# 4. delete directory 
os.rmdir("example")

os.unlink("students")

# 5. rename directory 
os.rename("students", "student-1")
print("students rename as student-1") 

# 6. 