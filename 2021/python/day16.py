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

length_types = {0: 15,
                1: 11}


def hex_string_to_bits(hex_string):
    return ''.join([hex_to_bits.get(c) for c in hex_string])


def bits_to_int(bits):
    return int(bits, 2)


def initial_assertions():
    assertions = {'D2FE28': {'bits': '110100101111111000101000',
                             'version': 6,
                             'type_id': 4},
                  '38006F45291200': {'bits': '00111000000000000110111101000101001010010001001000000000',
                                     'version': 1,
                                     'type_id': 6},
                  'EE00D40C823060': {'bits': '11101110000000001101010000001100100000100011000001100000',
                                     'version': 7,
                                     'type_id': 3}}
    for hex_string, expected in assertions.items():
        bits = hex_string_to_bits(hex_string)
        assert expected.get('bits') == bits
        assert expected.get('version') == bits_to_int(bits[:3])
        assert expected.get('type_id') == bits_to_int(bits[3:6])

    return


PACKET_TYPE_LITERAL = 4


def part1():
    initial_assertions()

    # python could probably do the translation for us, but let's do it ourselves, like santa intended
    bits = hex_string_to_bits('38006F45291200')
    version, type_id = bits_to_int(bits[:3]), bits_to_int(bits[3:6])
    if type_id != PACKET_TYPE_LITERAL:
        length_type_id = int(bits[6])
        start_idx = 7
        end_idx = start_idx + length_types.get(length_type_id)

        sub_packet_bit_length = int(bits[start_idx:end_idx], 2)
        start_idx = end_idx
        end_idx = start_idx + sub_packet_bit_length
        sub_packet = bits[start_idx:end_idx]

        sub_packet_version, sub_packet_type_id = bits_to_int(sub_packet[:3]), bits_to_int(sub_packet[3:6])
        if sub_packet_type_id == PACKET_TYPE_LITERAL:
            continuation_character_found = True
            digits = []
            while continuation_character_found:
                continuation_character = int(sub_packet[6])
                continuation_character_found = continuation_character == 1
                digits.append(int(sub_packet[7:11], 2))
            print(digits)

    print(f'bits: {bits}, version: {version}, type_id: {type_id}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
