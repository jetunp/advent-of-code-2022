# --- Part Two ---
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
# Initialize a list to keep track of the Calories carried by each Elf
elf_calories = []

# Open the input file (replace 'input.txt' with your input file name)
with open('../util/input.txt') as file:
    current_elf_calories = 0
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if line:  # Non-empty line, so add the Calories to the current Elf's total
            current_elf_calories += int(line)
        else:  # Blank line indicates a new Elf's inventory
            # Add current Elf's Calories to the list
            elf_calories.append(current_elf_calories)
            current_elf_calories = 0  # Reset the current Elf's Calories

    # Check the last Elf's Calories as there may not be a blank line at the end
    elf_calories.append(current_elf_calories)

# Sort the list of Elf Calories in descending order
elf_calories.sort(reverse=True)

# Calculate the sum of the Calories carried by the top three Elves
top_three_sum = sum(elf_calories[:3])

print("The top three Elves carrying the most Calories are carrying a total of:",
      top_three_sum, "Calories.")
