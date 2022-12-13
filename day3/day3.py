from string import ascii_letters

# Get the Data
with open('day3.in') as file:
    rucksacks = file.read().splitlines()

# Initialize sum
total_sum = 0

# Split rucksacks' content in half
for rucksack in rucksacks:
    n = len(rucksack)
    comp1 =  rucksack[0:n//2]
    comp2 = rucksack[n//2:]
    # print("Compartment 1: ", comp1)
    # print("Compartment 2: ", comp2)

    # Assign priority values to each letter
    values = dict()
    for priority, letter in enumerate(ascii_letters):
        # find common item in both compartments
        if letter in comp1 and letter in comp2:
            total_sum += priority + 1

print("Total sum: ", total_sum)
