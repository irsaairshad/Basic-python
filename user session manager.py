"""
User Session Manager (Instance Attributes) - SIMPLE

Ek system user profile ke liye User class banayein. Har user ka apna
username aur status = "Active" hona chahiye. Ek naya user object
banayein aur uska status print karein.
"""

class User:
    def __init__(self, username):
        self.username = username
        self.status = "Active"   # every new user starts as Active


new_user = User("irsa_dev")

print(f"Username: {new_user.username}")
print(f"Status: {new_user.status}")

"""
EXPLANATION:
- self.username and self.status are INSTANCE ATTRIBUTES -- each object
  created from the User class gets its OWN separate copy of them.
- 'status' is hard-coded to "Active" inside __init__, so EVERY new
  User object automatically starts with that status the moment it's
  created, without needing to pass it in manually.
- new_user = User("irsa_dev") creates one specific user object, and
  new_user.status simply reads that object's current status value.
"""
