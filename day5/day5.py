# Get data
# Separate crates from instructions
with open ('day5.in') as file:
    crates, instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

# print(crates)
# print(instructions)

# parse crates 
stacks = {int(digit):[] for digit in crates[-1].replace(" ", "")}

# find indexes of stacks
indexes = [index for index, char in enumerate(crates[-1]) if char != " "]

# display contents in each stack
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

# displayStacks()

def loadStacks():
    for string in crates[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ""
    for stack in stacks: 
        answer += stacks[stack][-1]
    return answer

loadStacks()
displayStacks()

# PART I 
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    num_crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    # start moving one crate at a time
    for crate in range(num_crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

print("Answer for Part I: ", getStackEnds())