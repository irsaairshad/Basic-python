class NetworkUtility:
    @staticmethod
    def is_latency_safe(latency):
        return latency <= 100


if __name__ == "__main__":
    print(NetworkUtility.is_latency_safe(45))
    print(NetworkUtility.is_latency_safe(150))
