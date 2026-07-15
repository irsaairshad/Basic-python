"""
Automated Tax Billing - INTERMEDIATE

Ek function calculate_bill(price, tax=5) banayein jahan tax ki
default value 5 ho. Function mein total bill return karein. Ek bar
tax pass kar ke aur ek bar bina tax pass kiye function call karein.
"""

def calculate_bill(price, tax=5):
    total = price + (price * tax / 100)
    return total

# Call WITHOUT passing tax -- uses the default value (tax=5)
bill_default = calculate_bill(1000)
print("Bill with default tax (5%):", bill_default)

# Call WITH a custom tax value passed in -- overrides the default
bill_custom = calculate_bill(1000, 12)
print("Bill with custom tax (12%):", bill_custom)

"""
EXPLANATION:
- tax=5 in the function definition is a DEFAULT PARAMETER VALUE: if
  the caller doesn't provide a 'tax' argument, Python automatically
  uses 5 in its place.
- calculate_bill(1000) only supplies 'price', so 'tax' falls back to
  its default of 5, calculating a 5% tax on top of the price.
- calculate_bill(1000, 12) supplies BOTH arguments, so the custom value
  12 overrides the default entirely for that specific call, calculating
  a 12% tax instead.
- This lets the same function handle the "common case" (5% tax) with
  minimal typing, while still being flexible enough to handle special
  cases when a different tax rate is needed.
"""
