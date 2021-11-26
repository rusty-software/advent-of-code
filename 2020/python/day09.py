with open("../input/day09.txt", "r") as fp:
    nums = [int(line.rstrip()) for line in fp.readlines()]


def sum_in(addends, target):
    diffs = {}
    for addend in addends:
        diff = target - addend
        if diff != addend:
            diffs[diff] = addend

    for diff in diffs.keys():
        if diff in addends:
            return True

    return False


def part1():
    preamble = 25
    targets = nums[preamble:]
    for target in targets:
        addends = nums[:preamble]
        if not sum_in(addends, target):
            print(f'No addends summing to target: {target}')
            break

        nums.pop(0)

    return


if __name__ == "__main__":
    part1()
    # 530627549
    # part2()
    # ?
