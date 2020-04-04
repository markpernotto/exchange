# exchange
A very simple Python API that returns static JSON data compiled from OpenExchangeRates.org. 

## objective
To setup an API that accepts 3 parameters: `source` identifies the source currency, `target` identifies the country we're exchanging our rate to, and `amount` is the amount of `source` currency we're looking to exchange. An optional, fourth parameter we'll accept is `date`, which is used to retrieve historical exchange rates.

## useage

clone the repository. `flask` is the only imported package. Once you've created your virtual environment, start the server like this: `python exchange.py`

In your browser/Postman/Insomnia/IDE API tool, use the URL your terminal provides, adding the `/exchange` route at the end

We faked the data:

`source` can be either `USD`, `JPY` or `HKD`

`target` can be either `USD`, `JPY` or `GBP`

`amount` should be a number - int or float

`date` can either be blank, `2020-04-01` or `2020-04-02`
