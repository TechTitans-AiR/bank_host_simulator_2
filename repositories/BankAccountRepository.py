

class BankAccountRepository:
    def find_by_card_number_cvc_and_expiration_date(self, card_number, cvc, expiration_date):
        from app import mongo
        query = {'cardNumber': card_number, 'cvc': cvc, 'expirationDate': expiration_date}
        result = mongo.db.cards.find_one(query)
        print("Query:", query)
        print("Result from database:", result)
        return result

        

    def find_all(self):
        from app import mongo
        return list(mongo.db.cards.find())

    def save(self, bank_account):
        try:
            from app import mongo

            
            if '_id' in bank_account:
                
                filter_query = {'_id': bank_account['_id']}

                
                bank_account.pop('_id', None)

                
                update_query = {'$set': bank_account}

                
                result = mongo.db.cards.update_one(filter_query, update_query)

                return result.modified_count > 0  
            else:
                
                print("Cannot update without _id.")
                return False
        except Exception as e:
            print("Error updating balance:", str(e))
            return False


    def find_by_id(self, bank_account_id):
        from app import mongo
        return mongo.db.cards.find_one({'_id': bank_account_id})
