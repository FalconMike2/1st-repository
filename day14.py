class GiftCart:
    def __init__(self):
        self.items = {}        # id -> price
        self.discount = 0.0    # current discount

        self.promos = {
            "PROMO10": 0.10,
            "PROMO25": 0.25,
            "SANTA50": 0.50
        }

    def add(self, gift_id, price):
        if price < 0:
            return
        if gift_id in self.items:
            return
        self.items[gift_id] = price

    def remove(self, gift_id):
        if gift_id in self.items:
            del self.items[gift_id]

    def applyDiscount(self, code):
        if code in self.promos:
            self.discount = self.promos[code]

    def total(self):
        total_price = sum(self.items.values())
        return total_price * (1 - self.discount)

    def clear(self):
        self.items = {}
        self.discount = 0.0

    def list(self):
        return self.items
