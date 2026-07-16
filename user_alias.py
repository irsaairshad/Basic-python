class UserProfile:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    user1 = UserProfile("Sara")
    user2 = user1  # aliasing, not a copy

    user2.name = "Ahmad"

    print("user1.name:", user1.name)
    print("user2.name:", user2.name)
    print("id(user1):", id(user1))
    print("id(user2):", id(user2))
    print("Same object:", user1 is user2)
