import utils
from collections import Counter

def process_data(filename):
    data = utils.read_file_lines_no_n(filename)
    data = [el.split("   ") for el in data]
    l_data, r_data = zip(*data)
    return list(l_data), list(r_data)

def part1(filename):
    l_data, r_data = process_data(filename)
    l_data.sort()
    r_data.sort()

    distance = 0
    for l, r in zip(l_data, r_data):
        distance += abs(int(l)-int(r))

    return distance

def part2(filename):
    l_data, r_data = process_data(filename)
    r_data_counts = Counter(r_data)

    sim_score = 0
    for l in l_data:
        sim_score += int(l)*r_data_counts[l]
    
    return sim_score



if __name__ == "__main__":
    # print(part1('data_files/day1.txt')) #1258579
    print(part2('data_files/day1.txt')) #23981443
    
