class WirelessModem:
    def connect(self):
        print("Connecting via WirelessModem...")


class AudioSpeaker:
    def connect(self):
        print("Connecting via AudioSpeaker...")


class SmartSpeaker(WirelessModem, AudioSpeaker):
    pass


if __name__ == "__main__":
    speaker = SmartSpeaker()
    speaker.connect()
    print("MRO order:", [cls.__name__ for cls in SmartSpeaker.__mro__])
