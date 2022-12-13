# Get the Data
with open('day3.in') as file:
    rucksacks = [i for i in file.read().strip().split('\n')]

# print(data)

# Split rucksacks' content in half
for rucksack in rucksacks:
    n = len(rucksack)
    comp1 =  rucksack[0:n//2]
    comp2 = rucksack[n//2:]
    print("Compartment 1: ", comp1)
    print("Compartment 2: ", comp2)
