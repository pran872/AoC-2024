import utils

def prepare_data(filename):
    data = utils.read_file_lines_no_newline(filename)
    data = [list(map(int, el.split(' '))) for el in data]
    return data 

def part1_is_safe(report):
    inc = report[1] > report[0]
    for level_no in range(1, len(report)):
        diff = abs(report[level_no-1] - report[level_no])
        # unsafe conds:
            # diff > 3, diff = 0, 
            # or (inc is True and level_no-1>level_no)
            # or (inc is False and level_no-1<level_no)
        if ((diff > 3) or 
            (diff == 0) or
            (inc and report[level_no-1]>=report[level_no]) or
            (not inc and report[level_no-1]<=report[level_no])):

            return False
    
    return True

def part1(filename):
    data = prepare_data(filename)

    safe_count = 0
    for report in data:
        safe_count += part1_is_safe(report)
    
    return safe_count

def part2_is_safe(report):

    inc = report[0] < report[1]
    for level_no in range(1, len(report)):
        diff = abs(report[level_no-1] - report[level_no])
        if ((diff > 3) or 
            (diff == 0) or
            (inc and report[level_no-1]>=report[level_no]) or
            (not inc and report[level_no-1]<=report[level_no])):
            
            new_report1 = report[:level_no] + report[level_no+1:]
            new_report2 = report[:level_no-1] + report[level_no:]
            
            # special case 1 4 3 2 1
            if level_no == 2:
                new_report3 = report[1:]
                inc = report[1] < report[2]
    
            if not(part1_is_safe(new_report1) or part1_is_safe(new_report2)):
                if level_no == 2 and part1_is_safe(new_report3):
                    return True
                return False
            else:
                return True
    return True
                

def part2(filename):
    data = prepare_data(filename)

    safe_count = 0
    for report in data:
        safe_count += part2_is_safe(report)
    
    return safe_count

if __name__ == "__main__":
    # print(part1('data_files/day2.txt')) #332
    print(part2('data_files/day2.txt')) #398
            
        