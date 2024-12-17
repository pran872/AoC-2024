import utils
import numpy as np
import copy

def prepare_data(filename):
    data = utils.get_grid(filename)
    return data

def check_bounds(antinode, data):
    x, y = antinode
    if x < len(data) and x > -1 and y < len(data[0]) and y > -1:
        return True
    else:
        return False

def get_antinode_locs(data, freq):
    freq_locs = np.where(data == freq)
    freq_locs = list(zip(*freq_locs))
    freq_locs = [tuple(map(int, l)) for l in freq_locs]

    antinode_locs = set()
    for i in range(0, len(freq_locs)-1):
        for j in range(i+1, len(freq_locs)):
            coord1, coord2 = np.array(freq_locs[i]), np.array(freq_locs[j])
            
            diff1 = coord1-coord2
            antinode1 = coord1+diff1

            antinode2 = coord2+(-diff1)

            if check_bounds(antinode1, data):
                antinode_locs.add(tuple(map(int, antinode1)))
            if check_bounds(antinode2, data):
                antinode_locs.add(tuple(map(int, antinode2)))
    return antinode_locs


def part2_get_antinode_locs(data, freq):
    freq_locs = np.where(data == freq)
    freq_locs = list(zip(*freq_locs))
    freq_locs = [tuple(map(int, l)) for l in freq_locs]

    antinode_locs = set()
    for i in range(0, len(freq_locs)-1):
        for j in range(i+1, len(freq_locs)):
            coord1, coord2 = np.array(freq_locs[i]), np.array(freq_locs[j])
            antinode_locs.add(tuple(map(int, coord1)))
            antinode_locs.add(tuple(map(int, coord2)))

            diff1 = coord1-coord2

            while check_bounds(coord1+diff1, data):
                antinode1 = coord1+diff1
                antinode_locs.add(tuple(map(int, antinode1)))
                coord1 = antinode1
            
            while check_bounds(coord2+(-diff1), data):
                antinode2 = coord2+(-diff1)
                antinode_locs.add(tuple(map(int, antinode2)))
                coord2 = antinode2

    return antinode_locs


def print_it(data, all_locs):
    for loc in all_locs:
        data[loc[0], loc[1]] = "#"
    for row in data:
        print("".join(row))
    

def part1(filename):
    data = prepare_data(filename)

    all_locs = set()
    for freq in np.unique(data):
        if freq != '.':
            locs = get_antinode_locs(data, freq)
            all_locs = all_locs.union(locs)
    
    print(len(all_locs))

def part2(filename):
    data = prepare_data(filename)

    all_locs = set()
    for freq in np.unique(data):
        if freq != '.':
            locs = part2_get_antinode_locs(data, freq)
            all_locs = all_locs.union(locs)
    
    print(len(all_locs))
    # print_it(data, all_locs)


if __name__ == "__main__":
    filename = "data_files/day8.txt"
    # part1(filename) # 390
    part2(filename) # 1246
