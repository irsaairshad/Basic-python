"""
Banned User Filter (System Logic) - SIMPLE

Ek Profile class banayein. Ek method restrict_access() likhein jo
user ka status "Banned" set kar de taake system use block kar sake.
"""

class Profile:
    def __init__(self, username):
        self.username = username
        self.status = "Active"   # every profile starts as Active

    def restrict_access(self):
        self.status = "Banned"


user_profile = Profile("spammer_123")
print(f"{user_profile.username} status before: {user_profile.status}")

user_profile.restrict_access()
print(f"{user_profile.username} status after:  {user_profile.status}")

"""
EXPLANATION:
- Every new Profile object starts with self.status = "Active", set
  inside the constructor.
- restrict_access(self) is a method that changes that same object's
  status attribute to "Banned" whenever it's called -- this is the
  action a system would trigger after detecting abusive behavior, for
  example.
- Once user_profile.restrict_access() runs, the rest of the system can
  check user_profile.status elsewhere in the code (e.g.
  "if profile.status == 'Banned': deny login") to block that user from
  further access.
"""
