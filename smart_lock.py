class SmartLock:
    def __init__(self, pin="0000"):
        self.__pin = pin
        self.state = "Locked"

    def set_pin(self, new_pin):
        if not isinstance(new_pin, str) or len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("Pin must be a 4 digit string containing only digits.")
        self.__pin = new_pin
        print("Pin updated successfully.")

    def unlock(self, input_pin):
        if input_pin == self.__pin:
            self.state = "Unlocked"
            print("System state changed to Unlocked.")
        else:
            print("Incorrect pin. Access denied.")
        return self.state


if __name__ == "__main__":
    lock = SmartLock()

    try:
        lock.set_pin("45a2")
    except ValueError as e:
        print(e)

    lock.set_pin("9081")
    lock.unlock("9081")
