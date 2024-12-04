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