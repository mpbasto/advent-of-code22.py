from utils.helpers import str_list


data = str_list('./inputs/day6-input.txt')

MARKER_1 = 4
MARKER_2 = 14

def char_processor(input, marker):
    buffer = input[0]
    for char in range(marker, len(buffer)):
        sub = set(buffer[:char][-marker:])
        if len(sub) == marker:
            return char

print(f'The answer for part 1 is: {char_processor(data, MARKER_1)}') # 1343
print(f'The answer for part 2 is: {char_processor(data, MARKER_2)}') # 2193