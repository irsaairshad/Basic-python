"""
Critical Server Bug Patching (Insert) - LISTS

Aapke paas daily tasks ki list hai:
tasks = ["Check Backup", "Update OS", "Send Report"].
Ek critical security bug report hota hai. Is task "Fix Critical Bug"
ko task list ke bilkul shuru mein (index 0) par insert karein aur
updated list print karein.
"""

tasks = ["Check Backup", "Update OS", "Send Report"]

print("Before:", tasks)

# .insert(index, item) places 'item' at the given 'index', shifting
# all existing elements from that position onward one step to the right.
tasks.insert(0, "Fix Critical Bug")

print("After: ", tasks)

"""
EXPLANATION:
- Unlike .append(), which always adds to the END of a list, .insert()
  lets you choose EXACTLY where the new item goes by specifying an
  index as the first argument: list.insert(index, value).
- tasks.insert(0, "Fix Critical Bug") inserts the new task at index 0
  (the very beginning), and everything that was already in the list
  automatically shifts one position to the right to make room -- so
  "Check Backup" moves from index 0 to index 1, and so on.
- This reflects real-world priority handling: the critical bug jumps
  to the front of the task queue instead of waiting at the end.
"""
