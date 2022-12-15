
def get_submatrix(l,r,c):
    new_matrix = []
    
    for row in l:
        new_matrix.append(row[:c]+row[c+1:])
        
    new_matrix.pop(r)
    
    return new_matrix

m = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

print(get_submatrix(m,2,1))