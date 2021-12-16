import time

with open("../input/day16.txt", "r") as fp:
    transmission = [line.rstrip() for line in fp.readlines()][0]


def with_perf_timing(fn, args=None):
    start_time = time.perf_counter()
    if args:
        fn(args)
    else:
        fn()
    end_time = time.perf_counter()
    print(f'Execution time: {end_time - start_time:0.6f}')


hex_to_bits = {'0': '0000',
               '1': '0001',
               '2': '0010',
               '3': '0011',
               '4': '0100',
               '5': '0101',
               '6': '0110',
               '7': '0111',
               '8': '1000',
               '9': '1001',
               'A': '1010',
               'B': '1011',
               'C': '1100',
               'D': '1101',
               'E': '1110',
               'F': '1111'}


def version_num(packet):
    return ""


def part1():
    hex_string = '0xD2FE28'
    bits = f'{int(hex_string, 16):b}'
    assert bits == '110100101111111000101000'
    s = '38006F45291200'
    hex_string = f'0x{s}'
    print(hex_string)
    bits = f'{int(hex_string, 16):b}'
    print(bits)
    assert bits == '00111000000000000110111101000101001010010001001000000000'
    # bits = hex_to_bits('EE00D40C823060')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
