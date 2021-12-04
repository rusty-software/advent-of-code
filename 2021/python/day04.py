with open("../input/day04.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


def parse_lines():
    hopper = []
    cards = []
    for row_idx, row in enumerate(lines):
        if row_idx == 0:
            hopper = row.split(',')
            continue

        if row == '':
            cards.append([])
            continue
        else:
            card_idx = len(cards) - 1
            cards[card_idx].append([(row[i:i + 3]).strip() for i in range(0, len(row), 3)])
    return hopper, cards


def find_num_pos_in_card(card, num):
    """
    Given a card and num, returns a list of the row and col indexes if the num is in the card, None otherwise.
    """
    for row_idx, row in enumerate(card):
        if num in row:
            return [row_idx, row.index(num)]
    return None


def bingo_check(found_nums):
    """
    Given a list of coordinates, returns a list of coordinates if all the coordinates in a row or column are present,
    otherwise None.
    """
    for idx in range(5):
        covered_rows = [coord for coord in found_nums if coord[0] == idx]
        covered_cols = [coord for coord in found_nums if coord[1] == idx]
        if len(covered_rows) == 5:
            print(f'bingo in row: {covered_rows}')
            return covered_rows
        if len(covered_cols) == 5:
            print(f'bingo in col: {covered_cols}')
            return covered_cols
    return False


def play(hopper, cards):
    marked_nums = dict()
    for num in hopper:
        for card_idx, card in enumerate(cards):
            num_pos = find_num_pos_in_card(card, num)
            if num_pos:
                if card_idx not in marked_nums.keys():
                    marked_nums[card_idx] = []
                marked_nums[card_idx].append(num_pos)
                bingo_coords = bingo_check(marked_nums[card_idx])
                if bingo_coords:
                    total = 0
                    for row_idx, row in enumerate(card):
                        for col_idx, col in enumerate(row):
                            if [row_idx, col_idx] not in marked_nums[card_idx]:
                                total += int(col)
                    return {'card_idx': card_idx,
                            'total': total,
                            'last_num': num,
                            'product': total * int(num)}


def part1():
    hopper, cards = parse_lines()
    winner = play(hopper, cards)
    print(f'total: {winner["total"]} * last num: {winner["last_num"]} = {winner["product"]}')

    return


if __name__ == "__main__":
    part1()
    # 69579
    # part2()
    #
