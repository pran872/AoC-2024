import numpy as np

def read_file_lines(filename):
    '''Returns list; each element is a line, each element ends with \n'''
    with open(filename, 'r') as f:
        return f.readlines()

def read_file_lines_no_newline(filename):
    with open(filename, 'r') as f:
        return f.read().strip().split('\n')

def read_file_as_one_no_newline(filename):
    with open(filename, 'r') as f:
        return f.read().strip().replace('\n', '')
    
def read_file(filename):
    '''Returns string'''
    with open(filename, 'r') as f:
        return f.read()
    
def read_file_2_sections(filename):
    with open(filename, 'r') as f:
        data = read_file(filename)
        data1, data2 = data.split("\n\n")
        data1 = data1.split('\n')
        data2 = data2.split('\n')
        
        return data1, data2

def get_grid(filename):
    data = read_file_lines_no_newline(filename)
    data = [list(i) for i in data]
    data = np.array(data)
    return data
