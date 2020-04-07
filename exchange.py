from flask import Flask, json, request
import datetime

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
    target = request.args.get('target')
    amount = request.args.get('amount')
    exchangeDate = request.args.get('date')

    # validation tests
    if source is None or amount is None or target is None:
        return 'minimum parameters are not set'

    _amount = validateAmount(amount)
    _source = str(source) if len(str(source)) == 3 else False
    _target = str(target) if len(str(target)) == 3 else False
    _exchangeDate = validateDate(exchangeDate) 

    if _amount == 0:
        return 'amount must be greater than 0 to get rate'

    if _exchangeDate is False:
        return "date must be valid date in YYYY-MM-DD format"

    # looping through our list
    if _source is not False and _target is not False:
        for e in exchanges:
            if _exchangeDate is not None:
                if 'date' in e:
                    if e['date'] == _exchangeDate and e['source'] == _source and e['target'] == _target:
                        return formatTargetAmount(e['exchange'], _amount)
            else: 
                if 'date' not in e:
                    if e['source'] == _source and e['target'] == _target:
                        return formatTargetAmount(e['exchange'], _amount)

    return 'no exchanges found'

def validateAmount(amount):
    try:
        return float(amount)
    except ValueError:
        return 0

def validateDate(exchangeDate):
    try:
        date = datetime.datetime.strptime(exchangeDate, '%Y-%m-%d')
        date = str(date)
        return date.split()[0]
    except ValueError:
        return False

def formatTargetAmount(exchange, amount):
    return str(exchange * amount)

if __name__ == '__main__':
    api.run()