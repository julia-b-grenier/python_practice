num_of_rows = 3
num_of_columns = 3

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for r in range(num_of_rows):
    # Sequence 0 ... number of rows-1
    print('Printing row', r)

    for c in range(num_of_columns):
        # Sequence 0 ... number of columns-1
        print(r, c, matrix[r][c])
