"""
Leaderboard Analytics - INTERMEDIATE

Ek gamer ke scores ki list banayein. max() aur min() ka istemal kar
ke highest aur lowest scores print karein.
"""

scores = [340, 780, 220, 990, 560]

highest_score = max(scores)   # built-in function: largest value in the list
lowest_score = min(scores)    # built-in function: smallest value in the list

print("All scores:", scores)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

"""
EXPLANATION:
- max(list) scans through every value in the list and returns the
  LARGEST one.
- min(list) does the same but returns the SMALLEST value.
- Both are built-in Python functions, so there's no need to manually
  loop through the list and compare values yourself -- Python handles
  that internally and gives you the answer directly.
"""
