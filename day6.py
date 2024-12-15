import utils
import numpy as np
import copy

def prepare_data(filename):
    data = utils.get_grid(filename)
    return data

def print_grid(data, curr_pos, curr_dir, pos_visited):

    for row_vist, col_visit in pos_visited:
        data[row_vist, col_visit] = "X"

    data[curr_pos[0], curr_pos[1]] = curr_dir
    print(data)


def print_grid_part2(data):
    for row in data:
        print("".join(row))

def one_loop(data, i=None):
    curr_dir = "^"
    mov_dict = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    rot_dict = {"^": ">", ">": "v", "v": "<", "<": "^"}
    syms = {"^": "|", "v": "|", ">": "-", "<": "-"}

    start = np.where(data == '^')
    row_no = int(start[0][0])
    col_no = int(start[1][0])
    
    old_data = copy.deepcopy(data)
    same_count = 0
    steps = 0
    while True:
        # print()
        # print_grid_part2(data)
        # print(steps, row_no, col_no)
        mov_row, mov_col = mov_dict[curr_dir]
        
        if (
            (row_no+mov_row < len(data) and row_no+mov_row>-1) and
            (col_no+mov_col < len(data[0]) and col_no+mov_col>-1)
        ):
            if data[row_no+mov_row, col_no+mov_col] == "#" or data[row_no+mov_row, col_no+mov_col] == "O":
                # print('inside')
                curr_dir = rot_dict[curr_dir]
                data[row_no, col_no] = "+"
                # print()
                # print_grid_part2(data)
            else:
                if i is not None and row_no+mov_row == i[0] and col_no+mov_col == i[1]:
                    # print('added', i)
                    if int(start[0][0]) == row_no+mov_row and int(start[1][0]) == col_no+mov_col:
                        return data, False
                    data[row_no+mov_row, col_no+mov_col] = "O"
                    i = None
                    # print_grid_part2(data)
                    continue
                    # exit()
                row_no += mov_row
                col_no += mov_col
                steps += 1
                if data[row_no, col_no] == "^" or data[row_no, col_no] == "+":
                    continue
                elif (
                    (data[row_no, col_no] == "-" and (curr_dir == "^" or curr_dir == "v")) or
                    (data[row_no, col_no] == "|" and (curr_dir == "<" or curr_dir == ">"))
                ):
                    data[row_no, col_no] = "+"
                else:
                    data[row_no, col_no] = syms[curr_dir]
                
                
                    
        else:
            return data, False

        # if same_count > 0:
        #     print("SAME", same_count)
        #     print("old")
        #     print_grid_part2(old_data)
        #     print("new")
        #     print_grid_part2(data)

        if np.array_equal(data, old_data):
            same_count += 1
            if same_count == 100:
                # print()
                # print()
                # print()
                # print("i am done")
                # exit()
                return data, True
        else:
            same_count = 0
            old_data = copy.deepcopy(data)
    



def part1(filename):
    data = prepare_data(filename)

    curr_dir = "^"
    mov_dict = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    rot_dict = {"^": ">", ">": "v", "v": "<", "<": "^"}

    start = np.where(data == '^')
    row_no = int(start[0][0])
    col_no = int(start[1][0])
    data[row_no, col_no] = "."
    pos_visited = set()

    while True:
        pos_visited.add((row_no, col_no))

        mov_row, mov_col = mov_dict[curr_dir]
        if (
            (row_no+mov_row < len(data) and row_no+mov_row>-1) and
            (col_no+mov_col < len(data[0]) and col_no+mov_col>-1)
        ):
            if data[row_no+mov_row, col_no+mov_col] == "#":
                # print()
                # print_grid(copy.deepcopy(data), (row_no, col_no), curr_dir, pos_visited)
                curr_dir = rot_dict[curr_dir]
            else:
                row_no += mov_row
                col_no += mov_col
        else:
            print(len(pos_visited))
            return len(pos_visited)

def part2(filename):
    data = prepare_data(filename)
    one_loop_data, _ = one_loop(copy.deepcopy(data))
    og_pos = np.where((one_loop_data != ".") & (one_loop_data != "#"))
    og_pos = list(zip(*og_pos))
    og_pos = [tuple(map(int, item)) for item in og_pos]
    # print()
    # print()
    # print()
    # print()
    # print()
    # print()
    res = 0
    for pos_no, (new_row, new_col) in enumerate(og_pos):
        print(f"{pos_no}/{len(og_pos)}")
        this, loops = one_loop(copy.deepcopy(data), (new_row, new_col))
            # print()
            # print_grid_part2(this)
        # print()
        # print_grid_part2(this)
        # print(loops)
        if loops:
            # print()
            # print("Looped")
            # print_grid_part2(this)
            res += 1
            # if i == 1:
            #     break

        # break
    print(res)
    


    
    
        

if __name__ == "__main__":
    filename = "data_files/day6.txt" 
    # part1(filename) # 5145
    part2(filename) #1523 

