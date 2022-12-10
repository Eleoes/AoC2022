# Get data
with open('day2.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# A/X = ROCK
# B/Y = PAPER
# C/Z = SCISSORS

# LOSE = 3
# DRAW = 3
# WIN = 6

# ----------------------------------------------------------------
# left vs right | outcome | right + outcome = total
# ----------------------------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN = (2 + 6) = 8
# A vs Z = LOSE = (3 + 0) = 3
# B vs X = LOSE = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN = (3 + 6) = 9
# C vs X = WIN = (1 + 6) = 7
# C vs Y = LOSE = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

score = 0

for round in data:
    score += outcomes[round]

# Print score

print("The total score is: ", score)

# PART II
real_score = 0

real_outcomes = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

for round in data:
    real_score += real_outcomes[round]
print("The real total score is: ", real_score)