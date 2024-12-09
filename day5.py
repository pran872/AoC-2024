import utils
import copy

def prepare_data(filename):
    rules, pages = utils.read_file_2_sections(filename)
    rules = [rule.split('|') for rule in rules]
    rules = [list(map(int, rule)) for rule in rules]
    pages = [page.split(',') for page in pages]
    pages = [list(map(int, page)) for page in pages]
    return rules, pages

def is_correct(update, the_rule_book):
    for ind, page in enumerate(update):
            
        for first_no, second_no in the_rule_book[page]:
            if first_no in update and second_no in update:
                if first_no == page:
                    second_ind = update.index(second_no)
                    if second_ind<ind:
                        return False
                else:
                    first_ind = update.index(first_no)
                    if first_ind>ind:
                        return False
                
    return True

def get_rule_book(rules):
    the_rule_book = {}

    for rule in rules:
        for no in rule:
            if no not in the_rule_book:
                the_rule_book[no] = [rule]
            else:
                the_rule_book[no].append(rule)

    return the_rule_book

def fix_update(update, the_rule_book):
    update_copy = copy.deepcopy(update)
    rel = []
    for page in update_copy:
        for first_no, second_no in the_rule_book[page]:
            if first_no in update_copy and second_no in update_copy:
                if [first_no, second_no] not in rel:
                    rel.append([first_no, second_no])

    for first_no, second_no in rel:
        ind_1 = update_copy.index(first_no)
        ind_2 = update_copy.index(second_no)
        if ind_1 > ind_2:
            update_copy.remove(first_no)
            update_copy.insert(ind_2, first_no)

    return update_copy[len(update_copy)//2], update_copy

def part1(filename):
    rules, pages = prepare_data(filename)
    the_rule_book = get_rule_book(rules)
    
    result = 0
    for update in pages:
        correct = is_correct(update, the_rule_book)
        
        if correct:
            result += update[len(update)//2]
    
    return result
                     
def part2(filename):
    rules, pages = prepare_data(filename)
    the_rule_book = get_rule_book(rules)

    result = 0
    for update in pages:
        if is_correct(update, the_rule_book):
            continue
        while not is_correct(update, the_rule_book):
            res, update = fix_update(update, the_rule_book)
        result += res

    return result
    

if __name__ == "__main__":
    filename = "data_files/day5.txt"
    # print(part1(filename)) #5588
    print(part2(filename)) #5331 