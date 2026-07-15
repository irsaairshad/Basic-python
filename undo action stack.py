"""
Undo Action Stack (Pop) - LISTS

Ek text editor user ke operations ko track kar raha hai:
actions = ["Type 'Hello'", "Make Bold", "Insert Table"].
User "Undo" button dabata hai. List method use karke action list ke
aakhri element ko nikalhein (pop karein) aur print karein ke kaunsa
action remove hua hai.
"""

actions = ["Type 'Hello'", "Make Bold", "Insert Table"]

print("Action history before undo:", actions)

# .pop() with NO index argument removes and RETURNS the LAST element
# of the list -- perfect for an "undo" feature, since the most recent
# action is always the last one added.
undone_action = actions.pop()

print("Undo performed. Action removed:", undone_action)
print("Action history after undo: ", actions)

"""
EXPLANATION:
- .pop() (called without arguments) removes the LAST item in the list
  and also RETURNS that removed value, so we can capture it in a
  variable (undone_action) to know exactly what was undone.
- This models a classic "stack" data structure (Last-In-First-Out):
  the most recently added action is the first one removed when undoing
  -- exactly how undo/redo systems work in real text editors.
- Note: .pop(index) can also remove an item from a SPECIFIC position
  if you pass an index, e.g. actions.pop(0) would remove the FIRST
  item instead.
"""
