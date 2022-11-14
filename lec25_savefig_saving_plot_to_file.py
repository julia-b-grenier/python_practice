import matplotlib.pyplot as plt


x_values = list(range(50))
y_values = []

for x in x_values:
    y_values.append(x ** 2)
    
plt.plot(x_values, y_values)

plt.title('An Amazing Plot', fontsize=16)
plt.xlabel('Some numbers', fontsize=14)
plt.ylabel('Squares', fontsize=14)

plt.savefig("plot_of_squares.png")