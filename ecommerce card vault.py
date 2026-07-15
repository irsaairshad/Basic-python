"""
E-Commerce Card Vault (Aggregation Security) - RELATIONSHIPS

Aapne Customer class aur CreditCard class ke darmiyan Aggregation
(Has-A) relationship banayi hai. Agar CreditCard class ka variable
__card_number private hai, toh kya Customer class us private value
ko direct search kar sakegi, ya use getter function ki zaroorat hogi?
"""

class CreditCard:
    def __init__(self, card_number):
        self.__card_number = card_number   # private attribute

    def get_card_number(self):
        return self.__card_number   # getter -- the ONLY proper way in


class Customer:
    def __init__(self, name, card):
        self.name = name
        self.card = card   # Aggregation: Customer HAS-A CreditCard object

    def show_card_details(self):
        # ATTEMPT 1 (would fail): self.card.__card_number
        # This does NOT work, because of Name Mangling -- it would look
        # for _Customer__card_number, not _CreditCard__card_number.

        # CORRECT WAY: go through the CreditCard's own getter method
        print(f"{self.name}'s card number: {self.card.get_card_number()}")


card = CreditCard("4111-2222-3333-4444")
customer = Customer("Ayesha", card)

customer.show_card_details()

"""
ANSWER: Customer class CANNOT directly access CreditCard's private
__card_number -- it NEEDS a getter method.

EXPLANATION:
- Private attributes (double underscore) are scoped to the class they
  are DEFINED in, not just "outside code in general." Because of Name
  Mangling, __card_number inside CreditCard actually becomes
  _CreditCard__card_number internally.
- Even though Customer HAS-A CreditCard object (Aggregation), Customer
  is still a completely SEPARATE, different class -- it has no special
  built-in permission to reach into CreditCard's private internals,
  just because it happens to hold a reference to a CreditCard object.
- The correct, safe approach is exactly what encapsulation is meant
  to enforce: CreditCard must expose a PUBLIC getter method (like
  get_card_number()), and Customer calls THAT method
  (self.card.get_card_number()) to retrieve the value properly,
  rather than ever touching __card_number directly.
"""
