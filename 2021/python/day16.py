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

packet_type_literal = 4


def hex_string_to_bits(hex_string):
    return ''.join([hex_to_bits.get(c) for c in hex_string])


def bits_to_int(bits, s):
    return int(bits, 2), s[len(bits):]


def bits_and_remaining(bits, s):
    return bits, s[len(bits):]


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
        original_bits = hex_string_to_bits(hex_string)
        bits = original_bits
        version, remaining_bits = bits_to_int(bits[:3], bits)
        type_id, remaining_bits = bits_to_int(remaining_bits[:3], remaining_bits)
        assert expected.get('bits') == original_bits
        assert expected.get('version') == version
        assert expected.get('type_id') == type_id

    return


def process_literal_packet(literals, remaining_bits):
    continuation_character_found = True
    while continuation_character_found:
        continuation_character, remaining_bits = bits_and_remaining(remaining_bits[0], remaining_bits)
        # print(f'continuation: {continuation_character}, remaining: (length: {len(remaining_bits)}) {remaining_bits}')
        continuation_character_found = int(continuation_character) == 1
        # print(f'continuation character found? {continuation_character_found}')
        literal, remaining_bits = bits_and_remaining(remaining_bits[:4], remaining_bits)
        # print(f'appending {literal} to {literals}')
        literals.append(literal)
        if not continuation_character_found:
            remaining_bits = ''
    return remaining_bits


def process_operator_packet(operators, remaining_bits):
    length_type_id, remaining_bits = bits_to_int(remaining_bits[0], remaining_bits)
    print(f'length_type_id: {length_type_id}, remaining_bits: (length {len(remaining_bits)}) {remaining_bits}')
    end_idx = length_types.get(length_type_id)
    print(f'end_idx: {end_idx}')
    sub_packet, remaining_bits = bits_and_remaining(remaining_bits[:end_idx], remaining_bits)
    print(f'sub_packet: {sub_packet}, remaining: {remaining_bits}')
    remaining_bits = ''
    return remaining_bits


def part1():
    initial_assertions()

    literals = []
    operators = []
    # python could probably do the translation for us, but let's do it ourselves, like santa intended
    # bits = hex_string_to_bits('D2FE28')
    bits = hex_string_to_bits('38006F45291200')
    version, remaining_bits = bits_to_int(bits[:3], bits)
    type_id, remaining_bits = bits_to_int(remaining_bits[:3], remaining_bits)
    print(f'version: {version}, type_id: {type_id}')
    while len(remaining_bits) > 0:
        print(f'continuing to process: (length: {len(remaining_bits)}) {remaining_bits}')
        if type_id == packet_type_literal:
            remaining_bits = process_literal_packet(literals, remaining_bits)
        else:
            remaining_bits = process_operator_packet(operators, remaining_bits)

    print(f'literals: {literals}')
    print(f'operators: {operators}')

    # version, type_id = bits_to_int(bits[:3]), bits_to_int(bits[3:6])
    # if type_id != packet_type_literal:
    #     length_type_id = int(bits[6])
    #     start_idx = 7
    #     end_idx = start_idx + length_types.get(length_type_id)
    #
    #     sub_packet_bit_length = int(bits[start_idx:end_idx], 2)
    #     start_idx = end_idx
    #     end_idx = start_idx + sub_packet_bit_length
    #     sub_packet = bits[start_idx:end_idx]
    #
    #     sub_packet_version, sub_packet_type_id = bits_to_int(sub_packet[:3]), bits_to_int(sub_packet[3:6])
    #     if sub_packet_type_id == packet_type_literal:
    #         continuation_character_found = true
    #         digits = []
    #         while continuation_character_found:
    #             continuation_character = int(sub_packet[6])
    #             continuation_character_found = continuation_character == 1
    #             digits.append(int(sub_packet[7:11], 2))
    #         print(digits)
    #
    # print(f'bits: {bits}, version: {version}, type_id: {type_id}')
    return


if __name__ == "__main__":
    with_perf_timing(part1)
    #
    # with_perf_timing(part2)
    #
