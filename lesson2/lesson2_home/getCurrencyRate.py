import urllib2
import json

def get_currency_rate(list_rate):
    url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22BYRUSD%2CBYREUR%2CBYRRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    data = urllib2.urlopen(url).read()
    parsed_data = json.loads(data)
    currency_rate = {}
    for item in parsed_data['query']['results']['rate']:
        rate = str(item['Name'])[:3]+str(item['Name'])[-3:]
        if rate in list_rate:
            currency_rate[rate] = float(item['Rate'])
    return currency_rate

print(get_currency_rate(['BYRUSD', 'BYREUR']))
