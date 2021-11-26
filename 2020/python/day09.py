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


def part2():
    target = 530627549

    print(f'target: {target}')
    for idx, num in enumerate(nums):
        current_sum = 0
        jdx = idx
        while current_sum < target:
            current_sum += nums[jdx]
            jdx += 1

        if current_sum == target:
            subrange = nums[idx:jdx]
            print(f'Range produced target! {subrange}')
            print(f'min: {min(subrange)}, max: {max(subrange)}')
            print(f'sum: {min(subrange) + max(subrange)}')
            return
        else:
            print(f'No range from {num} (idx {idx})')

    print('No range produced target!')

    return


if __name__ == "__main__":
    # part1()
    # 530627549
    part2()
    # 77730285
