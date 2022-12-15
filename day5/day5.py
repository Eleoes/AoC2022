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

loadStacks()
displayStacks()