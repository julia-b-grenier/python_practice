import matplotlib.pyplot as plt # submodule

# lect 25

some_numbers = [3,2,1,4,5,10]
plt.plot(some_numbers)

x_coords = range(0, 10, 2)
y_coords = [0, 0, 9, 8, 2]
plt.plot(x_coords, y_coords)

# linear function y = x + 5

x_coord = range(15)
y_coord = []
for x in x_coord:
    y_coord.append(x + 5)
plt.plot(x_coord, y_coord)


some_numbers = [3, 1, 5, 2, 9, 3]
plt.plot(some_numbers, "o--g")

plt.show()

mtl_pop = [1293992, 1080545, 1015420, 1016376, 1620693, 1704694]
years = ['1966', '1976', '1986', '1996', '2006', '2016']
plt.bar(years, mtl_pop)
plt.title("Population of Montreal")
plt.show()