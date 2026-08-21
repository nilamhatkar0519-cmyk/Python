# calc.py

# 1. Create and write data
def create_file():
    file = open("student.txt", "w")

    file.write("Name : Nilam Hatkar\n")
    file.write("Roll No : 70\n")
    file.write("Course : AJP\n")

    file.close()

    print("Student file created successfully.")


# 2. Read file
def read_file():
    file = open("student.txt", "r")

    print("----- Student Details -----")
    print(file.read())

    file.close()


# 3. Append data
def append_file():
    file = open("student.txt", "a")

    file.write("\nName : Sahil Patil\n")
    file.write("Roll No : 35\n")
    file.write("Course : AJP\n")

    file.close()

    print("Data appended successfully.")


# 4. Read after appending
def read_after_append():
    file = open("student.txt", "r")

    print("----- After Appending -----")
    print(file.read())

    file.close()


# 5. Write binary
def write_binary():
    file = open("student.txt", "wb")

    print("Bytes written:", file.write(b"Hello student!!"))

    file.close()


# 6. Read binary
def read_binary():
    file = open("student.txt", "rb")

    print(file.read())

    file.close()


# 7. Append binary
def append_binary():
    file = open("student.txt", "ab")

    data = file.write(b"How are you all ??")

    print("Bytes appended:", data)

    file.close()


# 8. read()
def read_method():
    file = open("student.txt", "r")

    data = file.read()

    print("----- read() -----")
    print(data)

    file.close()


# 9. readline()
def readline_method():
    file = open("student.txt", "r")

    print("----- readline() -----")
    print(file.readline())

    file.close()


# 10. readlines()
def readlines_method():
    file = open("student.txt", "r")

    print("----- readlines() -----")
    print(file.readlines())

    file.close()


# 11. tell()
def tell_method():
    file = open("student.txt", "r")

    print("Initial position:", file.tell())

    data = file.read(5)

    print("Data:", data)
    print("Current position:", file.tell())

    file.close()


# 12. seek()
def seek_method():
    file = open("student.txt", "r")

    print("Position:", file.seek(3))

    file.seek(0)

    print("Data:", file.read())

    file.close()