"""
Student Result Privacy - INTERMEDIATE

Ek dictionary banayein (name, roll_no, marks). Result hide karne ke
liye .pop() method use kar ke dictionary se marks remove karein aur
updated data dikhayein.
"""

student = {
    "name": "Fatima",
    "roll_no": "FA23-BCS-045",
    "marks": 88
}

print("Before hiding result:", student)

# dict.pop(key) removes the given key (and its value) from the
# dictionary, and also RETURNS the removed value if you want to use it.
removed_marks = student.pop("marks")

print("Marks removed:", removed_marks)
print("After hiding result: ", student)

"""
EXPLANATION:
- dictionary.pop(key) is used to remove a specific key-value pair from
  a dictionary, using the KEY as the reference point (similar in spirit
  to list.remove(value), but for dictionaries you always target a key,
  not a value).
- Here, student.pop("marks") removes the "marks" key entirely from the
  dictionary, and returns its value (88) so we can still use/print it
  separately if needed (e.g. for logging), while the main 'student'
  dictionary no longer contains that sensitive field.
- If "marks" didn't exist in the dictionary, .pop() would raise a
  KeyError -- you can avoid that by passing a default value, e.g.
  student.pop("marks", None).
"""
