import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175, 180]
weight = [50, 52, 55, 60, 65, 70, 75]

plt.scatter(height, weight)

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight")

plt.show()

##subplot 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [10, 20, 30, 40, 50]
y2 = [50, 40, 30, 20, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Increasing")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Decreasing")

plt.tight_layout()

plt.show()