import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.plot(x, y, marker="o")

plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Graph with Grid")

plt.grid(True)

plt.show()
