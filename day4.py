import utils
import numpy as np

def prepare_data(filename):
    data = utils.read_file_lines_no_newline(filename)
    arr = np.array(list(map(list, data)))
    return arr

def part1_check_dir(arr, curr_cord, word, the_dir):
    row, col = curr_cord
    word_ind = 1
    
    while word_ind < len(word):
        if (
            (row < 0) or
            (row >= (len(arr))) or
            (col < 0) or
            (col >= (len(arr[0]))) or
            (word[word_ind] != arr[row, col])
        ):
            return False

        row += the_dir[0]
        col += the_dir[1]
        word_ind += 1
    
    return True

def part1_word_search(arr, curr_cord, word):
    matches = 0

    row, col = curr_cord[0], curr_cord[1]
    for i in range(row-1, row+2):
        if i >= 0 and i < len(arr):
            for j in range(col-1, col+2):
                if j>= 0 and j < len(arr[0]):
                    
                    if arr[i, j] == word[1]:
                        the_dir = (i-row, j-col)
                        match = part1_check_dir(arr, (i, j), word, the_dir)
                        if match:
                            matches += 1
    return matches

def part2_word_search(arr, curr_cord):
    check_cords = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)] ]

    for up, down in check_cords:
        new_up = (curr_cord[0]+up[0], curr_cord[1]+up[1])
        new_down = (curr_cord[0]+down[0], curr_cord[1]+down[1])

        up_char = arr[new_up[0], new_up[1]]
        down_char = arr[new_down[0], new_down[1]]
        if f"{up_char}{down_char}"  not in ["MS", "SM"]:
            return False
    
    return True

def part1(filename):
    arr = prepare_data(filename)
    word = list('XMAS')
    matches = 0
    # try brute force first

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "X":
                matches += part1_word_search(arr, (i, j), word)
    
    return matches

def part2(filename):
    arr = prepare_data(filename)
    matches = 0

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i, j] == 'A':
                matches += part2_word_search(arr, (i, j))

    return matches

if __name__ == "__main__":
    filename = 'data_files/day4.txt'
    # print(part1(filename)) #2447
    print(part2(filename)) #1868