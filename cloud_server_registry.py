class CloudServer:
    __active_servers_count = 0

    def __init__(self):
        CloudServer.__active_servers_count += 1
        self.server_id = f"Server-{100 + CloudServer.__active_servers_count}"

    @classmethod
    def get_active_count(cls):
        return cls.__active_servers_count


if __name__ == "__main__":
    s1 = CloudServer()
    s2 = CloudServer()
    s3 = CloudServer()

    print([s.server_id for s in (s1, s2, s3)])
    print("Active servers:", CloudServer.get_active_count())
