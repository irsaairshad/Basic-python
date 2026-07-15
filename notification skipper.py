"""
Notification Skipper - INTERMEDIATE

1 se 10 tak user IDs ko for loop se traverse karein. Jab ID 5 aaye
(jo banned user hai), toh continue statement ka istemal kar ke usay
skip kar dein aur baki IDs par notification bhejein.
"""

for user_id in range(1, 11):
    if user_id == 5:
        continue   # skip the rest of THIS iteration and jump to the next one
    print(f"Sending notification to User ID {user_id}")

"""
EXPLANATION:
- range(1, 11) generates numbers 1 through 10 (11 is excluded), giving
  us all 10 user IDs to loop through.
- 'continue' immediately skips the REST of the current loop iteration
  and jumps straight to the next one -- so when user_id == 5, the
  print() statement below it never runs for that specific ID, but the
  loop keeps going normally for 6, 7, 8, 9, 10 afterward.
- This is different from 'break', which would stop the ENTIRE loop
  completely -- 'continue' only skips ONE iteration and carries on.
"""
