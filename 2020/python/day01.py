with open('../input/day01.txt', 'r') as f:
    lines = f.readlines()

expenses = [int(line.split("\n")[0]) for line in lines]


def find_pair_improved(expected_sum):
    """
    Seems like this algorithm would scale linearly.

    Tanya told me about this one (she's gone through an algorithms course)
    """
    diffs = {}
    for expense in expenses:
        diffs[expected_sum - expense] = expense

    for expense in expenses:
        if expense in diffs.keys():
            return expense, diffs[expense]


def find_triple_improved(expected_sum):
    """
    Sorting and two-pointer technique

    I looked this one up. Seems reasonable that it would be a better performer than the n^3.
    """
    # sort the array. ah, mutability
    expenses.sort()

    upperbound = len(expenses)
    # fix the first of the triple values and try to find the other two values
    for i in range(0, upperbound - 2):
        # start the pointers at opposite eligible ends of the array
        left = i + 1
        right = upperbound - 1

        while left < right:
            current_sum = expenses[i] + expenses[left] + expenses[right]
            if current_sum == expected_sum:
                return expenses[i], expenses[left], expenses[right]
            elif current_sum < expected_sum:
                # too small: move the left pointer
                left += 1
            else:
                # too large: move the right pointer
                right -= 1

    return None, None, None


def calc():
    [left, right] = find_pair_improved(2020)
    print('find_pair_improved: {:d} * {:d} == {:d}'.format(left, right, left * right))
    # 444019
    [left, middle, right] = find_triple_improved(2020)
    print('find_triple_improved: {:d} * {:d} * {:d} == {:d}'.format(left, middle, right, left * middle * right))
    # 29212176


if __name__ == "__main__":
    calc()
