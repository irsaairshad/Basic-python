"""
Banned User System Cleanup (Remove) - LISTS

Ek active community users ki list hai:
members = ["ali_dev", "banned_user_10", "sara_ux", "zain_qa"].
System scan ke baad aapko "banned_user_10" ko remove karna hai.
Value-based list method use karke use remove karein aur clean list
print karein.
"""

members = ["ali_dev", "banned_user_10", "sara_ux", "zain_qa"]

print("Before cleanup:", members)

# .remove(value) searches the list for the FIRST matching value and
# deletes it -- this is "value-based" removal, as opposed to removing
# by index/position (like .pop(index) does).
members.remove("banned_user_10")

print("After cleanup: ", members)

"""
EXPLANATION:
- list.remove(value) is the value-based removal method: you tell it
  WHAT to remove (the actual value, "banned_user_10"), not WHERE it is
  (its index). Python searches the list and removes the first item
  that matches.
- This is different from .pop(index), which removes an item based on
  its POSITION (covered in Question 12), or 'del list[index]', which
  also works by index.
- If the value doesn't exist in the list, .remove() raises a
  ValueError -- so it's good practice to check membership first with
  `if "banned_user_10" in members:` in a real system, though the
  question just asks for the direct removal.
"""
