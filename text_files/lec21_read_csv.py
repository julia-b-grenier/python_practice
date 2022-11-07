"""
A comma-separated values (CSV) file stores tabular data by using commas to separate values.

Spreadsheet software (Excel, Numbers) can directly open a CSV file and display it in spreadsheet format

"""

def read_csv(csv_filename):
    """ (str) -> list<str)
    """
    
    matrix = []
    fobj = open(csv_filename, "r")
    
    for line in fobj:        
        row = line.strip().split(",")
        matrix.append(row)
        
    fobj.close()
    return matrix