from utils.helpers import str_list

def solve_part_1(data):
    elf = {"A": 1, "B": 2, "C": 3} # Column 1
    me = {"X": 1, "Y": 2, "Z": 3} # Column 2
    scores = {"L": 0, "D": 3, "W": 6}
    totals = 0

    for line in data:
        shape1, shape2 = line.split()
        x = elf[shape1]
        y = me[shape2]

        match y - x:
            case 0:
                round = "D"
            case -2 | 1:
                round = "W"
            case -1 | 2:
                round = "L"

        totals += y + scores[round]

    return totals

def solve_part_2(data):
    elf = {"A": 1, "B": 2, "C": 3}
    me = {"X": 0, "Y": 3, "Z": 6}
    totals = 0

    for line in data:
        shape1, shape2 = line.split()
        x = elf[shape1]
        round_score = me[shape2]

        match round_score:
            case 6:  # Win
                y = x % 3 + 1
            case 3:  # Draw
                y = x
            case 0:  # Loss
                y = (x + 1) % 3 + 1

        totals += y + round_score

    return totals


games = str_list('./inputs/day2-input.txt')
print(f'The answer for part 1 is: {solve_part_1(games)}')
print(f'The answer for part 2 is: {solve_part_2(games)}')
    