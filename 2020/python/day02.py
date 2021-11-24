with open('../input/day02.txt', 'r') as f:
    lines = f.readlines()

password_data = [line.split("\n")[0] for line in lines]


def part1():
    valid_count = 0
    for pwd in password_data:
        [min_max, letter, password] = pwd.split(' ')
        [min_count, max_count] = min_max.split('-')
        letter = letter[0]
        letters = ''.join((filter(lambda x: x == letter, password)))
        if int(min_count) <= len(letters) <= int(max_count):
            valid_count += 1

    print('Valid password count: {:d}'.format(valid_count))


def part2():
    valid_count = 0
    for pwd in password_data:
        [min_max, letter, password] = pwd.split(' ')
        [min_loc, max_loc] = min_max.split('-')
        letter = letter[0]
        min_loc = int(min_loc) - 1
        max_loc = int(max_loc) - 1
        if (password[min_loc] == letter or password[max_loc] == letter) \
                and not (password[min_loc] == letter and password[max_loc] == letter):
            valid_count += 1

    print('Valid password count: {:d}'.format(valid_count))


if __name__ == "__main__":
    part1()
    # 546
    part2()
    # 275
