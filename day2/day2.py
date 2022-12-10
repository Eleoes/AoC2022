# Get data
with open('day2.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# print(data)

X, Y, Z = 'X', 'Y', 'Z'
A, B, C = 'A', 'B', 'C'


lose = 0
draw = 3
win = 6

col1 = []
col2 = []

score = 0

if X in data[0]:
    score += 1
elif Y in data[0]:
    score += 2
elif Z in data[0]:
    score += 3

print(score)

# for round in data:
#     col1.append(round[0])
#     col2.append(round[2])
# print(col2)


# Get total score for one round
    # Get score of shape
    # Get score of outcome

# Get total score for all rounds
