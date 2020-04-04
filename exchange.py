from flask import Flask, json, request

# crudely done to represent exchange rates by date
exchanges = [
        {
            "source": "USD",
            "exchange": 108.429,
            "target": "JPY"
        }, 
        {
            "source": "USD",
            "exchange": 108.033, 
            "target": "JPY",
            "date": "2020-04-02"
        },
        {
            "source": "USD",
            "exchange": 107.29594444,
            "target": "JPY",
            "date": "2020-04-01"
        },
        {
            "source": "JPY",
            "exchange": 0.009223,
            "target": "USD"
        },
        {
            "source": "JPY",
            "exchange": 0.009256,
            "target": "USD",
            "date": "2020-04-02"
        },
        {
            "source": "JPY",
            "exchange": 0.00932,
            "target": "USD",
            "date": "2020-04-01"
        },
        {
            "source": "HKD",
            "exchange": 0.105155,
            "target": "GBP"
        },
        {
            "source": "HKD",
            "exchange": 0.104106,
            "target": "GBP",
            "date": "2020-04-02"
        },
        {
            "source": "HKD",
            "exchange": 0.104185,
            "target": "GBP",
            "date": "2020-04-01"
        }
    ]

api = Flask(__name__)

@api.route('/exchange', methods=['GET'])
def get_exchanges():
    source = request.args.get('source')
    amount = request.args.get('amount')
    target = request.args.get('target')
    exchangeDate = request.args.get('date')

    for e in exchanges:
        if e['source'] == source and e['target'] == target:
            return str(e['exchange'] * int(amount))
        else:
            return "not found"

if __name__ == '__main__':
    api.run()