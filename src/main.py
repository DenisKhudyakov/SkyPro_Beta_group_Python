import json

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.processing import sorted_operation

if __name__ == "__main__":
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

    print(
        sorted_operation(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
