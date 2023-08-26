# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
opponent_move = ''
expected_outcome = ''
your_score = 0
score_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
with open('../util/input.txt') as file:
    for line in file:
        values = line.split()
        opponent_move, expected_outcome = values[0], values[1]
        # draw scenario
        if (opponent_move == 'A' and expected_outcome == 'Y') or (opponent_move == 'B' and expected_outcome == 'Y') or (opponent_move == 'C' and expected_outcome == 'Y'):
            your_score += 3+score_dict[opponent_move]
        # win scenario
        if (opponent_move == 'A' and expected_outcome == 'Z'):
            your_score += 6+score_dict['Y']
        elif (opponent_move == 'B' and expected_outcome == 'Z'):
            your_score += 6+score_dict['Z']
        elif (opponent_move == 'C' and expected_outcome == 'Z'):
            your_score += 6+score_dict['X']
        # Lose scenario
        if (opponent_move == 'A' and expected_outcome == 'X'):
            your_score += score_dict['Z']
        elif (opponent_move == 'B' and expected_outcome == 'X'):
            your_score += score_dict['X']
        elif (opponent_move == 'C' and expected_outcome == 'X'):
            your_score += score_dict['Y']
print("Your total score:", your_score)
