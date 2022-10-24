
matrix = [[1,2,3],[4,5,6],[7,8,9]]

def matrix_row_sum(my_list):
    sums = []
    for r in range(len(my_list)):
        row_sum = 0
        for c in range(len(my_list[0])):
            row_sum += my_list[r][c]
        sums.append(row_sum)
    return sums


def matrix_col_sum(my_list):
    sums = []
    for c in range(len(my_list[0])):
        col_sum = 0
        for r in range(len(my_list)):
            col_sum += my_list[r][c]
        sums.append(col_sum)
    return sums