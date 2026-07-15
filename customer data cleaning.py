"""
Customer Data Cleaning - INTERMEDIATE

Ek system mein duplicate email IDs list mein aagayi hain. Us list ko
pehle set mein convert karein taake duplicates uṛ jayen, phir .add()
use kar ke ek naya email add karein aur print karein.
"""

emails = ["ali@mail.com", "sara@mail.com", "ali@mail.com", "zain@mail.com"]

print("Original list (with duplicates):", emails)

# Converting to a set automatically removes duplicate values
unique_emails = set(emails)
print("After converting to set (duplicates removed):", unique_emails)

# .add() inserts a single new item into a set
unique_emails.add("hina@mail.com")
print("After adding a new email:", unique_emails)

"""
EXPLANATION:
- set(emails) rebuilds the data as a set, which by definition can only
  hold UNIQUE values -- so the duplicate "ali@mail.com" automatically
  collapses down to just one entry.
- .add(value) is the set method used to insert a single new item into
  an existing set (this is the set equivalent of .append() for lists).
- Note: since sets are unordered, printed order may differ from the
  order items were added -- that's expected, normal set behavior, not
  an error in the code.
"""
