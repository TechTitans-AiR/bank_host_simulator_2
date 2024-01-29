from models.BankAccount import BankAccount
from repositories.BankAccountRepository import BankAccountRepository
import datetime

class BankAccountService:
    def __init__(self):
        self.bank_account_repository = BankAccountRepository()

    def get_all_cards(self):
        bank_accounts = self.bank_account_repository.find_all()
        return [self.map_to_cards_dto(bank_account) for bank_account in bank_accounts]

    def map_to_cards_dto(self, bank_account):
        return {
            'cardNumber': bank_account['card_number'],
            'cvc': bank_account['cvc'],
            'expirationDate': bank_account['expiration_date'],
            'balance': bank_account['balance']
        }

    def get_all_bank_accounts(self):
        return self.bank_account_repository.find_all()

    def find_bank_account(self, card_number, cvc, expiration_date):
        print("Searching for card with number:",card_number)
        print("Searching for card with cvc:",cvc)
        print("Searhing for card with expiration date", expiration_date)

        
        optional_bank_account = self.bank_account_repository.find_by_card_number_cvc_and_expiration_date(card_number, cvc,expiration_date)
        print("Result from database:", optional_bank_account)

        if optional_bank_account:
            print("Card found:", optional_bank_account)

            
            card_document = optional_bank_account
        else:
            print("Card not found.")
            card_document = None

        return card_document


    def check_sufficient_funds(self, bank_account, requested_amount):
        return bank_account['balance'] >= requested_amount

    def check_card_expiration(self, bank_account):
        try:
            date_parts = bank_account['expirationDate'].split("-")
            year = int(date_parts[0])
            month = int(date_parts[1])

            current_date = datetime.datetime.now().date()

            return (year > current_date.year) or (year == current_date.year and month >= current_date.month)
        except Exception as e:
            print("Error checking card expiration:", str(e))
            return False





    def update_balance(self, bank_account, amount):
        try:
            if not self.check_card_expiration(bank_account):
                print("Card has expired.")
                return False

            new_balance = bank_account['balance'] - amount
            bank_account['balance'] = new_balance

            self.bank_account_repository.save(bank_account)
            return True
        except Exception as e:
            print("Error updating balance:", str(e))
            return False
