#Getting data from day1.in
with open('day1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# print (data)

#Loop through data
max = 0
max2 = 0   
max3 = 0
sum = 0
# elves = []
for item in data:
    # separate elves and
    # compare the sum of each elf's calories
    if item == '':
        # elves.append(sum)
        sum = 0
    else: 
        # convert the string to number
        num = int(item)
        # sum the numbers 
        sum += num
    if sum > max:
        max3 = max2
        max2 = max
        max = sum
    elif sum > max2:
        max3 = max2
        max2 = sum
    elif sum > max3:
        max3 = sum

#print highest value
# elves.sort()
# print(elves)
print("The number of calories carried by the elf carrying the MOST calories is: ", max)

# part 2: find the top three elves carrying the most calories.
# how many calories are those elves carrying in total?

print("The top three elves carrying the most calories are carrying: ", max+max2+max3)

