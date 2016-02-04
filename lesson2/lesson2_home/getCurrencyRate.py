import urllib2
import json
import  pprint


def get_currency_rate(list_rate):
    for index_rate in range(1, len(list_rate)):
        list_rate[index_rate] = '%2C' + list_rate[index_rate]
    url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%' \
          '22{}%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'.format(''.join(list_rate))
    data = urllib2.urlopen(url).read()
    parsed_data = json.loads(data)
    # pprint.pprint(parsed_data)
    currency_rate = {}
    for item in parsed_data['query']['results']['rate']:
        rate = str(item['Name'])[:3]+str(item['Name'])[-3:]
        currency_rate[rate] = float(item['Rate'])
    return currency_rate


if __name__ == "__main__":
    dir_rate = get_currency_rate(['USDBYR', 'EURBYR', 'BYRUSD', 'BYREUR', 'RUBBYR', 'BYRRUB', 'USDRUB', 'RUBUSD'])
    for rate in dir_rate:
        print('%s=%.5f' % (rate, dir_rate[rate]))

