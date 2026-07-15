"""
Tweet Text Analyzer - HARD

Ek function banayein jo ek string (jaise koi tweet) input le. For
loop se string ke har character par traverse karein. Agar woh
.isalpha() hai, toh Vowels aur Consonants ko alag alag count karein,
aur dono (2 values) ek sath return karein.
"""

def analyze_tweet(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():          # only count actual letters (skip spaces, numbers, punctuation)
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


tweet = "Python is amazing! #coding2026"
vowels_found, consonants_found = analyze_tweet(tweet)

print("Tweet:", tweet)
print("Vowels:", vowels_found)
print("Consonants:", consonants_found)

"""
EXPLANATION:
- The for loop goes through the string ONE CHARACTER at a time.
- char.isalpha() checks whether that character is a LETTER (True for
  'a'-'z' / 'A'-'Z', False for spaces, digits, punctuation, emoji,
  hashtags, etc.) -- this filters out anything that isn't a real letter
  before we try to classify it.
- If it IS a letter, we check whether it's in the string "aeiouAEIOU"
  (covering both lowercase and uppercase vowels) to decide whether to
  increment vowel_count or consonant_count.
- 'return vowel_count, consonant_count' returns BOTH values together as
  a tuple, which is why we can "unpack" them into two separate
  variables at the call site: vowels_found, consonants_found = ...
"""
