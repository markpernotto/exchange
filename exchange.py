from flask import Flask, json, request

exchanges = [
        {
            "source": "USD",
            "exchange": 108.429,
            "target": "JPY"
        }, 
    ]

api = Flask(__name__)

@api.route('/exchange', methods=['GET'])
def get_exchange():
    return json.dumps(exchanges)

if __name__ == '__main__':
    api.run()