"""
Question 04: Contact Directory - SIMPLE

Ek dictionary banayein jismein aapke dost ka name aur phone_number
ho. Phir us dost ka phone number update kar ke nayi dictionary print
karein.
"""

contact = {
    "name": "Bilal",
    "phone_number": "03001112222"
}

print("Before update:", contact)

# Dictionaries are mutable -- update a value by referencing its key
contact["phone_number"] = "03219998888"

print("After update: ", contact)

"""
EXPLANATION:
- A dictionary stores data as key-value pairs: {key: value, key: value}.
  Here, "name" and "phone_number" are the KEYS, and "Bilal" /
  "03001112222" are their corresponding VALUES.
- To update a value, you reference the dictionary by its key and
  assign a new value: contact["phone_number"] = "03219998888". This
  works because dictionaries (like lists) are MUTABLE -- you can
  change their contents after creation without rebuilding them.
- If the key already exists, this OVERWRITES the old value; if the
  key didn't exist yet, this same syntax would simply ADD a new
  key-value pair to the dictionary.
"""
