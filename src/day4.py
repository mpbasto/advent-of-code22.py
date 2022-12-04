import re
from utils.helpers import str_list

def fully_containing_pairs(pairs):
    total = 0
    for elf1start, elf1end, elf2start, elf2end in pairs:
        total += elf1start <= elf2start <= elf2end <= elf1end or elf2start <= elf1start <= elf1end <= elf2end
    return total

def total_overlapping_pairs(pairs):
    total = 0
    for elf1start, elf1end, elf2start, elf2end in pairs:
        total += max(elf1start, elf2start) <= min(elf1end, elf2end)
    return total

data = str_list('./inputs/day4-input.txt')
regex = '(\d+)-(\d+),(\d+)-(\d+)'
pairs = []

for pair in data:
    matching = re.match(regex, pair)
    pairs.append(tuple(map(int, matching.groups())))

print(f'The answer for part 1 is: {fully_containing_pairs(pairs)}') # 657
print(f'The answer for part 2 is: {total_overlapping_pairs(pairs)}') # 938