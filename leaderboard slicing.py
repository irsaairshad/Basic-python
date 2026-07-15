"""
 Leaderboard Slicing - LISTS

Ek online multiplayer game ke highest scores ki list hai. Slicing
operations ka use karke top 3 players ke scores (index 0 se 2) alag
karein aur unhein print karein.
"""

leaderboard_scores = [9800, 9500, 9200, 8700, 8300, 7900]

# Slicing syntax: list[start : stop]  -- 'stop' is EXCLUSIVE, so
# [0:3] grabs indices 0, 1, and 2 (i.e. the first three items).
top_3 = leaderboard_scores[0:3]

print("All scores:", leaderboard_scores)
print("Top 3 players' scores:", top_3)

"""
EXPLANATION:
- Slicing lets you pull out a sub-section of a list without a loop:
  list[start:stop] returns a NEW list containing elements from
  'start' up to (but NOT including) 'stop'.
- leaderboard_scores[0:3] means "start at index 0, stop before index 3",
  which gives us indices 0, 1, 2 -- exactly the first three (highest)
  scores, since the list is already ordered from highest to lowest.
- Note: leaderboard_scores[:3] (omitting the 0) works identically --
  when 'start' is left out, Python assumes it means "from the
  beginning".
"""
