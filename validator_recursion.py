import sys


class Validator:
    def validate(self):
        print("Base validation passed.")
        return True


class StrictValidatorBuggy(Validator):
    def validate(self):
        print("Running strict checks...")
        return self.validate()  # bug: calls itself instead of super().validate()


class StrictValidatorFixed(Validator):
    def validate(self):
        print("Running strict checks...")
        return super().validate()


if __name__ == "__main__":
    fixed = StrictValidatorFixed()
    fixed.validate()

    buggy = StrictValidatorBuggy()
    try:
        sys.setrecursionlimit(500)
        buggy.validate()
    except RecursionError as e:
        print("RecursionError caught:", e)
