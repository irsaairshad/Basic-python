"""
Streaming Service Track (Parameterized Constructor) - SIMPLE

Ek Song class banayein jahan __init__ constructor ke zariye user
naye song ka title aur artist object banate waqt hi pass kar sake.
"""

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


song1 = Song("Blinding Lights", "The Weeknd")
song2 = Song("Levitating", "Dua Lipa")

print(f"Now Playing: {song1.title} by {song1.artist}")
print(f"Now Playing: {song2.title} by {song2.artist}")

"""
EXPLANATION:
- This is called a PARAMETERIZED CONSTRUCTOR -- unlike a default
  constructor (which takes no extra input), __init__(self, title,
  artist) requires the caller to supply values for 'title' and
  'artist' the moment the object is created.
- Song("Blinding Lights", "The Weeknd") passes those two values
  directly into the constructor, which immediately stores them as
  self.title and self.artist on that specific song object.
- This lets each Song object be fully set up with its own real data
  right from the start, instead of being created empty and filled in
  later.
"""
