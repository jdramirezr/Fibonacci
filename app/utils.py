
def fibonacci():
    f1 = 1
    f2 = 1
    count = 2
    set_nums = set('123456789')

    while True:
        f1, f2 = f2, f1 + f2
        count += 1 
        str_num = str(f2)
        
        if set_nums == set(str_num[-9:]) and set_nums == set(str_num[:9]):
            break

    return count
