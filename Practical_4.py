# 1. student grade management system 
students = []
grades = []
def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    students.append(name)
    grades.append(grade)

    print("Student added successfully.")

def update_grade():
    name = input("Enter student name to update: ")

    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student name to remove: ")

    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully.")
    else:
        print("Student not found.")

def average_grade():
    if len(grades) == 0:
        print("No students available.")
    else:
        average = sum(grades) / len(grades)
        print("Average grade:", average)

def highest_lowest():
    if len(grades) == 0:
        print("No students available.")
    else:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Average grade")
    print("5. Highest and lowest grade")
    print("6. Display all students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        update_grade()

    elif choice == 3:
        remove_student()

    elif choice == 4:
        average_grade()

    elif choice == 5:
        highest_lowest()

    elif choice == 6:
        if len(students) == 0:
            print("No students available.")
        else:
            for i in range(len(students)):
                print(students[i], ":", grades[i])

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
        

# 2. manages the positions of points in a 2D plane
import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d
def farthest_point(points):
    farthest = points[0]
    max_distance = distance(farthest, (0, 0))
    for point in points:
        d = distance(point, (0, 0))
        if d > max_distance:
            max_distance = d
            farthest = point
    return farthest

n = int(input("Enter number of points: "))
points = []
for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    point = (x, y)
    points.append(point)
    
print("\nPoints:", points)
print("\nCalculate distance between two points")

p1_index = int(input("Enter index of first point: "))
p2_index = int(input("Enter index of second point: "))
p1 = points[p1_index]
p2 = points[p2_index]

print("Distance:", distance(p1, p2))
farthest = farthest_point(points)
print("Farthest point from origin:", farthest)
print("Distance from origin:", distance(farthest, (0, 0)))

# 3. Server configuration
server_ip = tuple(input("Enter server IP: ").split("."))
n = int(input("Enter number of allowed IPs: "))
allowed_ips = []

for i in range(n):
    ip = input("Enter allowed IP: ")
    allowed_ips.append(ip)

def update_allowed_ips():
    ip = input("Enter new IP to allow: ")
    allowed_ips.append(ip)
    print("IP added successfully.")

def display_configuration():
    print("\n--- Server Configuration ---")
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)

display_configuration()
update_allowed_ips()
display_configuration()
print("\nServer IP cannot be changed because it is stored as a tuple.")

# 4.employee projects

n1 = int(input("Enter number of employees in Project 1: "))
project1 = set()
for i in range(n1):
    name = input("Enter employee name: ")
    project1.add(name)

n2 = int(input("\nEnter number of employees in Project 2: "))
project2 = set()
for i in range(n2):
    name = input("Enter employee name: ")
    project2.add(name)

both_projects = project1.intersection(project2)

only_project1 = project1.difference(project2)
only_project2 = project2.difference(project1)

all_employees = project1.union(project2)

print("\n--- Employee Analysis ---")

print("Project 1 employees:", project1)
print("Project 2 employees:", project2)

print("\nEmployees working on both projects:", both_projects)

print("Employees working only on Project 1:", only_project1)

print("Employees working only on Project 2:", only_project2)

print("Total unique employees:", all_employees)

 
# 5. Take paragraph from user

text = input("Enter a paragraph: ")
text = text.lower()
words = text.split()
total_words = len(words)
frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")

    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nTotal number of words:", total_words)
print("\nWord Frequency:")

for word, count in frequency.items():
    print(word, ":", count)
    
sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)
print("\nTop 3 most frequent words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

vowels = "aeiou"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
print("\nTotal number of vowels:", vowel_count)


# 6. # Take text of Book 

book1 = input("Enter text of Book 1: ")
book2 = input("Enter text of Book 2: ")

words1 = set(book1.lower().split())
words2 = set(book2.lower().split())

print("\nUnique words in Book 1:")
print(words1)

print("\nUnique words in Book 2:")
print(words2)

common_words = words1.intersection(words2)

print("\nCommon words in both books:")
print(common_words)

only_book1 = words1.difference(words2)

print("\nWords unique to Book 1:")
print(only_book1)

only_book2 = words2.difference(words1)

print("\nWords unique to Book 2:")
print(only_book2)

all_words = words1.union(words2)
print("\nTotal number of unique words:", len(all_words))

