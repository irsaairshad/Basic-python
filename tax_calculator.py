class TaxCalculator:
    def calculate_tax(self, income, treaty_rate=None):
        if treaty_rate is None:
            tax = income * 0.10
            print(f"Local tax for income {income}: {tax}")
        else:
            tax = income * treaty_rate
            print(f"International tax for income {income} at treaty rate {treaty_rate}: {tax}")
        return tax


if __name__ == "__main__":
    calc = TaxCalculator()
    calc.calculate_tax(100000)
    calc.calculate_tax(100000, 0.15)
