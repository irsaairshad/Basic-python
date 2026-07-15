"""
Up-Next Playlist - INTERMEDIATE

5 songs ki ek list banayein. List Slicing ka istemal karte hue index
1 se 4 tak ke beech wale 3 songs ko "Up Next" queue ke tor par print
karein.
"""

songs = ["Intro Beat", "Sunset Drive", "Night Falls", "Golden Hour", "Fade Out"]

# Slicing syntax: list[start:stop] -- 'stop' is EXCLUSIVE.
# songs[1:4] grabs indices 1, 2, and 3 (three songs in between).
up_next = songs[1:4]

print("Full playlist:", songs)
print("Up Next queue:", up_next)

"""
EXPLANATION:
- The full list has 5 songs at indices 0, 1, 2, 3, 4.
- songs[1:4] means "start at index 1, and stop BEFORE index 4", which
  gives us indices 1, 2, and 3 -- exactly 3 songs, skipping the very
  first song (index 0, already playing) and the very last song (index
  4, not yet queued).
- This matches "index 1 se 4 tak ke beech wale 3 songs" -- the 3 songs
  sitting between the first and last positions.
"""
