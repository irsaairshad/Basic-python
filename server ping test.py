"""
Server Ping Test - SIMPLE

Ek for loop aur range(1, 6) ka istemal karte hue 5 mukhtalif servers
ke liye "Pinging Server X..." print karein.
"""

for server_number in range(1, 6):
    print(f"Pinging Server {server_number}...")

"""
EXPLANATION:
- range(1, 6) generates a sequence of numbers starting at 1 and going
  up to (but NOT including) 6 -- so it produces 1, 2, 3, 4, 5, which
  is exactly 5 numbers, one for each server.
- The for loop takes each of those numbers, one at a time, and stores
  it in 'server_number' for that pass through the loop, then runs the
  print() statement using that value inside an f-string.
- This avoids writing 5 separate print() statements manually -- the
  loop handles repeating the action for each server number
  automatically.
"""
