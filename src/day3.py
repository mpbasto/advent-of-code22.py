from utils.helpers import str_list       

data = str_list('./inputs/day3-input.txt')

def priority(char):
    item = ord(char)
    if item >= ord('a'):
        return item - ord('a') + 1
    return item - ord('A') + 27

# Part 1
total_priorities = 0
for rucksack in data:
    middle = len(rucksack) // 2
    matching = set(rucksack[:middle]).intersection(set(rucksack[middle:]))
    total_priorities += priority(list(matching)[0])

print(f'The answer for part 1 is: {total_priorities}') # challenge input: 7845


# Part 2
badges = 0
groups = list(map(set, data))
for i in range(0, len(data), 3):
    match = set.intersection(*groups[i:i+3])
    badges += priority(list(match)[0])

print(f'The answer for part 2 is: {badges}') # challenge input: 2790