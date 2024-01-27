from flask import Blueprint, request, jsonify
from services.BankAccountService import BankAccountService

cards_controller_bp = Blueprint('cards_controller', __name__)
bank_account_service = BankAccountService()

@cards_controller_bp.route('/api/v1/transactions', methods=['GET'])
def get_all_cards():
    cards_dto_list = bank_account_service.get_all_cards()
    return jsonify(cards_dto_list), 200

@cards_controller_bp.route('/api/v1/transactions/getAllBankAccounts', methods=['GET'])
def get_all_bank_accounts():
    all_bank_accounts = bank_account_service.get_all_bank_accounts()
    return jsonify(all_bank_accounts), 200

@cards_controller_bp.route('/api/v1/transactions/processTransaction', methods=['POST'])
def process_transaction():
    transaction_request = request.get_json()

    print("Transaction request data:", transaction_request)

    is_transaction_successful = process_transaction_request(transaction_request)

    response = {'status': 'approved' if is_transaction_successful else 'declined'}
    return jsonify(response), 200

def process_transaction_request(transaction_request):
    optional_bank_account = bank_account_service.find_bank_account(
        transaction_request.get('cardNumber'), transaction_request.get('cvc'),transaction_request.get('expirationDate')
    )

    if optional_bank_account:
        bank_account = optional_bank_account

        if not bank_account_service.check_card_expiration(bank_account):
            print("Card expired.")
            return False

        if bank_account_service.check_sufficient_funds(bank_account, transaction_request.get('balance')):
            if bank_account_service.update_balance(bank_account, transaction_request.get('balance')):
                return True
            else:
                print("Error updating balance.")
        else:
            print("Insufficient funds.")
    else:
        print("Card not found.")

    return False
