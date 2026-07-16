class PaymentGateway:
    name = "Generic Gateway"
    fee_percent = 0

    def process_payment(self, amount):
        fee = amount * self.fee_percent
        print(f"Processing transaction of {amount} amount via {self.name} with {fee} fee")
        return fee


class JazzCash(PaymentGateway):
    name = "JazzCash"
    fee_percent = 0.02


class EasyPaisa(PaymentGateway):
    name = "EasyPaisa"
    fee_percent = 0.015


class NayaPay(PaymentGateway):
    name = "NayaPay"
    fee_percent = 0.01


if __name__ == "__main__":
    gateways = [JazzCash(), EasyPaisa(), NayaPay()]
    for gateway in gateways:
        gateway.process_payment(1000)
