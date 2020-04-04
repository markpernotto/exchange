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

    # are any of the minimum parameters not set?
    if source is None or amount is None or target is None:
        return 'minimum parameters are not set'

    for e in exchanges:
        # make sure 'date' is a parameter and 'date' exists in our list
        if 'date' in request.args and 'date' in e:
            exchangeDate = request.args.get('date')
            if e['date'] == exchangeDate and e['source'] == source and e['target'] == target:
                return str(e['exchange'] * int(amount))
        else: 
            if e['source'] == source and e['target'] == target and 'date' not in e and 'date' not in request.args:
                return str(e['exchange'] * int(amount))

    return 'no exchanges found'

if __name__ == '__main__':
    api.run()