import utils
from itertools import product as it_prod

def prepare_data(filename):
    data = utils.read_file_lines_no_newline(filename)
    new_data = []
    for d in data:
        test, nos = d.split(": ")
        all_nos = nos.split(" ")
        all_nos = list(map(int, all_nos))
        new_data.append([int(test), all_nos])

    return new_data

def true_test(input):
    test_value, nos = input[0], input[1]

    perms = list(it_prod(["add", "mult"], repeat=len(nos)-1))
    
    for perm in perms:
        for i, op in enumerate(perm):
            if op == 'add':
                if i == 0:
                    res = nos[i] + nos[i+1]
                else:
                    # print('here', res, nos[i])
                    res += nos[i+1]
            elif op == "mult":
                if i == 0:
                    res = nos[i] * nos[i+1]
                else:
                    res = res*nos[i+1]
        # print(nos)
        # print(perm)
        # print(res)
        # print()
        if res == test_value:
            return True, test_value

    return False, test_value

def part_2_true_test(input):
    test_value, nos = input[0], input[1]

    perms = list(it_prod(["add", "mult", "||"], repeat=len(nos)-1))
    
    for perm in perms:
        for i, op in enumerate(perm):
            if op == 'add':
                if i == 0:
                    res = nos[i] + nos[i+1]
                else:
                    # print('here', res, nos[i])
                    res += nos[i+1]
            elif op == "mult":
                if i == 0:
                    res = nos[i] * nos[i+1]
                else:
                    res = res*nos[i+1]
            elif op == "||":
                if i == 0:
                    res = int(str(nos[i])+str(nos[i+1]))
                else:
                    res = int(str(res)+str(nos[i+1]))
                    
        # print(nos)
        # print(perm)
        # print(res)
        # print()
        if res == test_value:
            return True, test_value

    return False, test_value 

def part1(filename):
    data = prepare_data(filename)

    result = 0
    for input in data:
        is_true, test_value = true_test(input)
        if is_true:
            result += test_value

    print(result)

def part2(filename):
    data = prepare_data(filename)
    result = 0
    for input in data:
        is_true, test_value = part_2_true_test(input)
        if is_true:
            result += test_value

    print(result)

        

if __name__ == "__main__":
    filename = "data_files/day7.txt"
    # part1(filename) #6231007345478
    part2(filename) #333027885676693
