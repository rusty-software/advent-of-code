with open("../input/day10.txt", "r") as fp:
    nums = [int(line.rstrip()) for line in fp.readlines()]

test_nums = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4
]


def part1():
    nums.sort()
    last_num = 0
    gaps = {}
    for num in nums:
        diff = num - last_num
        print(f'current num: {num}, last num: {last_num}, diff: {diff}')
        if diff not in gaps.keys():
            gaps[diff] = 1
        else:
            gaps[diff] += 1
        last_num = num

    gaps[3] += 1
    print(gaps)
    print(f'product: {gaps[1]} * {gaps[3]} = {gaps[1] * gaps[3]}')
    return


if __name__ == "__main__":
    part1()
    # ?
    # part2()
    # ?
