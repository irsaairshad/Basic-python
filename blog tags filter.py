"""
Blog Tags Filter (Duplicates) - SIMPLE

Ek list mein blog tags hain: ["tech", "python", "tech"]. Is list ko
set mein convert karein taake duplicate "tech" khatam ho jaye, aur
unique tags print karein.
"""

blog_tags = ["tech", "python", "tech"]

# Converting a list to a set automatically removes duplicate values,
# since sets by definition can only contain UNIQUE elements.
unique_tags = set(blog_tags)

print("Original list:", blog_tags)
print("Unique tags (set):", unique_tags)

"""
EXPLANATION:
- A set is an unordered collection of UNIQUE items -- it cannot
  contain duplicate values by design.
- Calling set(blog_tags) takes every item from the list and drops any
  repeated values automatically, leaving only one "tech" instead of two.
- Note: sets are unordered, so the printed order of unique_tags may
  not match the original list order -- that's expected set behavior,
  not an error.
"""
