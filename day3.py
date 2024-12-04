import utils

def prepare_data(filename):
    return utils.read_file(filename)

def check_mul_match(data, left):
    pattern = ["m", "u", "l", "(", "number",  ",", "number", ")"]
    potential_numbers = []
    pattern_ind = 1
    right = left + 1

    while pattern_ind < len(pattern):
        if pattern_ind == 4:
            if data[right].isnumeric():
                potential_numbers.append(data[right])
                right += 1
            elif data[right] == ",":
                potential_numbers.append(data[right])
                right += 1
                pattern_ind += 2
            else:
                left = right
                break
        elif pattern_ind == 6:
            if data[right].isnumeric():
                potential_numbers.append(data[right])
                right += 1
            elif data[right] == ")":
                ''' successful find '''
                no1, no2 = "".join(potential_numbers).split(",")
                left = right+1
                return int(no1)*int(no2), left
            else:
                left = right
                break
        else:
            if data[right] == pattern[pattern_ind]:
                right += 1
                pattern_ind += 1
            else:
                left = right
                break
    return False, left

def check_dos_match(data, left, pattern):
    pattern = list(pattern)
    pattern_ind = 1
    right = left + 1

    while pattern_ind < len(pattern):
        if data[right] == pattern[pattern_ind]:
            right += 1
            pattern_ind += 1
        else:
            left += 1
            return False, left
    
    left += 1
    return True, left

def part1(filename):
    data = prepare_data(filename)

    left = 0
    count = 0
    while left < len(data):
        if data[left] == "m":
            match, left = check_mul_match(data, left)
            if match:
                count += match
        else:
            left += 1
                
    return count

def part2(filename):
    data = prepare_data(filename)

    left = 0
    count = 0
    do = True

    while left < len(data):
        if do and data[left] == "m":
            match, left = check_mul_match(data, left)
            if match:
                count += match
        elif data[left] == "d":
            dont_match, temp_left = check_dos_match(data, left, "don't()")
            if dont_match:
                do = False
                left = temp_left
            else:
                do_match, temp_left = check_dos_match(data, left, "do()")
                if do_match:
                    do = True
                    left = temp_left
                else:
                    left += 1
        else:
            left += 1
    return count



if __name__ == "__main__":
    # print(part1('data_files/day3.txt')) #156388521
    print(part2('data_files/day3.txt')) # 75920122

