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


def bin_nums_with_digit_at_idx(nums, digit, idx):
    return [bin_num for bin_num in nums if bin_num[idx] == digit]


def part2():
    digits_per_num = len(bin_nums[0])

    oxygen_generator_rating_candidates = bin_nums
    co2_scrubber_rating_candidates = bin_nums
    for digit_idx in range(digits_per_num):
        # oxygen generator rating
        if len(oxygen_generator_rating_candidates) > 1:
            zeros = bin_nums_with_digit_at_idx(oxygen_generator_rating_candidates, "0", digit_idx)
            ones = bin_nums_with_digit_at_idx(oxygen_generator_rating_candidates, "1", digit_idx)
            if len(zeros) <= len(ones):
                oxygen_generator_rating_candidates = ones
            else:
                oxygen_generator_rating_candidates = zeros

        # co2 scrubber rating
        if len(co2_scrubber_rating_candidates) > 1:
            zeros = bin_nums_with_digit_at_idx(co2_scrubber_rating_candidates, "0", digit_idx)
            ones = bin_nums_with_digit_at_idx(co2_scrubber_rating_candidates, "1", digit_idx)
            if len(zeros) <= len(ones):
                co2_scrubber_rating_candidates = zeros
            else:
                co2_scrubber_rating_candidates = ones

    oxygen_generator_rating = oxygen_generator_rating_candidates[0]
    co2_scrubber_rating = co2_scrubber_rating_candidates[0]
    print(f'oxygen generator rating: {oxygen_generator_rating}; co2 scrubber rating: {co2_scrubber_rating}')
    print(f'{int(oxygen_generator_rating, 2)} * {int(co2_scrubber_rating, 2)} = {int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)}')
    return


if __name__ == "__main__":
    # part1()
    # 1071734
    part2()
    # 6124992
