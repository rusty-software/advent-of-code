with open("../input/day05.txt", "r") as fp:
    lines = [line.rstrip() for line in fp.readlines()]


def string_to_point(string_point):
    return [int(x) for x in string_point.split(',')]


def endpoints_to_points(var_start, var_end, const_idx, const_idx_val):
    line = []
    rs = min([var_start, var_end])
    re = max([var_start, var_end])
    for z in range(rs, re + 1):
        if const_idx == 0:
            line.append([const_idx_val, z])
        else:
            line.append([z, const_idx_val])

    return line


def line_to_points(unparsed_data):
    start, end = unparsed_data.split(' -> ')
    start = string_to_point(start)
    end = string_to_point(end)
    if start[0] == end[0]:
        return endpoints_to_points(start[1], end[1], 0, start[0])
    elif start[1] == end[1]:
        return endpoints_to_points(start[0], end[0], 1, start[1])

    return None


def increment_touches(point_touches, points):
    for p in points:
        point = tuple(p)
        if point in point_touches:
            point_touches[point] += 1
        else:
            point_touches[point] = 1

    return


def count_gte_touches(point_touches, threshold):
    keep_count = 0
    for k, v in point_touches.items():
        if v >= threshold:
            keep_count += 1

    return keep_count


def part1():
    point_touches = dict()
    for line in lines:
        points = line_to_points(line)
        if points:
            increment_touches(point_touches, points)

    overlaps = count_gte_touches(point_touches, 2)
    print(f'overlaps: {overlaps}')
    return


if __name__ == "__main__":
    part1()
    # 7269
    # part2()
    #
