from src.generators import *
import json

if __name__ == '__main__':
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
        usd_transactions = filter_by_currency(transactions, "RUB")
        for _ in range(2):
            print(next(usd_transactions)["id"])
        descriptions = transaction_descriptions(transactions)
        for _ in range(5):
            print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)