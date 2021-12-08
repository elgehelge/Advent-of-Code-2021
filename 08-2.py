# Puzzle #2
import itertools

index2segment = 'abcdefg'  # 0 -> 'a'
segment2index = {c: i for i, c in enumerate('abcdefg')}  # 'a' -> 0
digits = [frozenset(d.replace('-', '')) for d in [
    'abc-efg',  # 0
    '--c--f-',  # 1
    'a-cde-g',  # 2
    'a-cd-fg',  # 3
    '-bcd-f-',  # 4
    'ab-d-fg',  # 5
    'ab-defg',  # 6
    'a-c--f-',  # 7
    'abcdefg',  # 8
    'abcd-fg',  # 9
]]
digits_mapping = {d: i for i, d in enumerate(digits)}  # set('abcefg') -> 0


def rewire(digit, wire_config):
    return frozenset([index2segment[wire_config[segment2index[seg]]] for seg in digit])


def search_wire_config(notes):
    for wire_config in itertools.permutations(range(7)):
        count_valid_digits = 0
        for digit in notes:
            rewired = rewire(digit, wire_config)
            if rewired not in digits:
                break
            count_valid_digits += 1
        if len(notes) == count_valid_digits:
            return wire_config
    raise ValueError('Wire config not found!')


def parse_line(line):
    notes_, display_ = line.split('|')
    notes, display = notes_.split(), display_.split()
    return notes, display


input_ = open('08-2-input.txt').readlines()
total = 0
for line in input_:
    notes, display = parse_line(line)
    wire_config = search_wire_config(notes)
    display_digits = [digits_mapping[rewire(digit, wire_config)] for digit in display]
    total += eval(''.join(map(str, display_digits)).lstrip('0'))
print(total)
