"""
Latency Monitor (Max/Min) - LISTS

Aapki system monitoring script ne database queries ki latencies
(in milliseconds) save ki hain. Built-in functions ka use karke sub
se fast query execution time (minimum value) aur sub se slow query
execution time (maximum value) find karke print karein.
"""

latencies_ms = [45, 120, 33, 98, 210, 15, 67]

fastest = min(latencies_ms)   # built-in function: smallest value in the list
slowest = max(latencies_ms)   # built-in function: largest value in the list

print("Recorded latencies (ms):", latencies_ms)
print("Fastest query execution time:", fastest, "ms")
print("Slowest query execution time:", slowest, "ms")

"""
EXPLANATION:
- Python provides two built-in functions specifically for this:
    min(list)  -> returns the smallest value in the list
    max(list)  -> returns the largest value in the list
- Since latency is measured in time (milliseconds), the SMALLEST value
  represents the FASTEST query (took the least time), and the LARGEST
  value represents the SLOWEST query (took the most time).
- Both functions scan through every element of the list automatically
  -- no manual loop or comparison logic is needed.
"""
