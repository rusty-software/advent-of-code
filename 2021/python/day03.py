with open("../input/day03.txt", "r") as fp:
    bin_nums = [line.rstrip() for line in fp.readlines()]


def part1():
    zero_sums = []
    one_sums = []
    for bin_num in bin_nums:
        for idx, digit in enumerate(bin_num):
            if len(zero_sums) <= idx:
                zero_sums.append(0)
                one_sums.append(0)

            if digit == "0":
                zero_sums[idx] += 1
            else:
                one_sums[idx] += 1

    print(f'zero_sums: {zero_sums}; one_sums: {one_sums}')

    gamma_rate = ""
    epsilon_rate = ""
    for idx, zero_sum in enumerate(zero_sums):
        one_sum = one_sums[idx]
        if zero_sum > one_sum:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    print(f'gamma_rate: {gamma_rate}; epsilon_rate: {epsilon_rate}')
    print(f'gamma val: {int(gamma_rate, 2)}; '
          f'epsilon val: {int(epsilon_rate, 2)}; '
          f'product: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

    return


if __name__ == "__main__":
    part1()
    #
    # part2()
    #
