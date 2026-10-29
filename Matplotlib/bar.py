import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "Computer"]
marks = [85, 90, 78, 95]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()


##horizontal bar chart
import matplotlib.pyplot as plt

students = ["Rahul", "Amit", "Priya", "Sneha"]
marks = [75, 88, 92, 81]

plt.barh(students, marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Performance")

plt.show()