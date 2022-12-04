with open('inputs/day1-input.txt', 'r') as data:
    elves = []
    for elf in data.read().split("\n\n"):
        elves.append(sum(map(int, elf.split())))

elves = sorted(elves, reverse=True) 
print(f'Part one: {elves[0]}') # 66306
print(f'Part two: {sum(elves[:3])}') # 195292
