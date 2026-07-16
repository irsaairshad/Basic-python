class DBSession:
    def __init__(self, host, port, user):
        self.credentials = (host, port, user)


if __name__ == "__main__":
    session = DBSession("localhost", 5432, "admin")
    print(session.credentials)

    try:
        session.credentials[1] = 8080
    except TypeError as e:
        print("Error:", e)
