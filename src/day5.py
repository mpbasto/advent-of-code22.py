from collections import defaultdict
import re

# PART 1
part1_stacks = defaultdict(list)

with open('./inputs/day5-input.txt') as data:
	instr = 'move'
	crate = '['
	regex_match = r'\d+'
	part1_output = ''
	for line in data:
		if crate in line:
			for i in range(1, len(line) - 1, 4):
				if line[i] != ' ':
					part1_stacks[(i - 1) // 4].append(line[i])
		elif line.startswith(instr):
			a, b, c = map(int, re.findall(regex_match, line))
			part1_stacks[c - 1] = part1_stacks[b - 1][:a][::-1] + part1_stacks[c - 1]
			part1_stacks[b - 1] = part1_stacks[b - 1][a:]
	
	for i in range(len(part1_stacks)):
		part1_output += part1_stacks[i][0]


print(f'The answer for part 1 is: {part1_output}') # NTWZZWHFV

# PART 2
part2_stacks = defaultdict(list)

with open('./inputs/day5-input.txt') as data:
	instr = 'move'
	crate = '['
	regex_match = r'\d+'
	part2_output = ''
	for line in data:
		if crate in line:
			for i in range(1, len(line) - 1, 4):
				if line[i] != ' ':
					part2_stacks[(i - 1) // 4].append(line[i])
		elif line.startswith(instr):
			a, b, c = map(int, re.findall(regex_match, line))
			part2_stacks[c - 1] = part2_stacks[b - 1][:a] + part2_stacks[c - 1]
			part2_stacks[b - 1] = part2_stacks[b - 1][a:]


	for i in range(len(part2_stacks)):
		part2_output += part2_stacks[i][0]

print(f'The answer for part 2 is: {part2_output}') # BRZGFVBTJ