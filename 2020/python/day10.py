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
        if diff not in gaps.keys():
            gaps[diff] = 1
        else:
            gaps[diff] += 1
        last_num = num

    gaps[3] += 1
    print(nums)
    print(gaps)
    print(f'product: {gaps[1]} * {gaps[3]} = {gaps[1] * gaps[3]}')
    return


def part2():
    """
    Yeah, this is an algorithm that I didn't bother to attempt.
    Solution once again kindly provided by the Internet.
    https://dev.to/qviper/advent-of-code-2020-python-solution-day-10-30kd
    """
    nums.sort()
    sol = {0: 1}
    for num in nums:
        sol[num] = 0
        if num - 1 in sol:
            sol[num] += sol[num - 1]
        if num - 2 in sol:
            sol[num] += sol[num - 2]
        if num - 3 in sol:
            sol[num] += sol[num - 3]

    print(sol[max(nums)])
    return


if __name__ == "__main__":
    part1()
    # 2516
    part2()
    # ?
