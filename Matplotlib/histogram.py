import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 72, 75, 78, 80,
         82, 85, 88, 90, 92, 95, 96, 98, 70, 65]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")

plt.show()
