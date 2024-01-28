

class BankAccount:
    def __init__(self, card_number, expiration_date, balance, cvc):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.balance = balance
        self.cvc = cvc

    def json(self):
        return {
            'card_number': self.card_number,
            'expiration_date': self.expiration_date,
            'balance': self.balance,
            'cvc': self.cvc
        }

    def save(self):
        from app import mongo
        mongo.db.cards.insert_one(self.json())
