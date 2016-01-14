#-*- coding:utf8 -*-
import csv
import pprint
import urllib2
import json

def get_currency_rate(list_rate):
    try:
        url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDBYR%2CEURBYR%2CBYRBYR%2CRUBBYR%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
        data = urllib2.urlopen(url).read()
        parsed_data = json.loads(data)
        currency_rate = {}
        for item in parsed_data['query']['results']['rate']:
            rate = str(item['Name'])[:3]+str(item['Name'])[-3:]
            if rate in list_rate:
                currency_rate[rate] = float(item['Rate'])
        return currency_rate
    except urllib2.HTTPError:
        print('error')

def parsing_csv_file_and_total_number_of_money_spent(file_table_with_data):
    #table = [row[:-1] for row in csv.reader(infile)]
    table = []
    total_number_of_money_spent = 0
    currency_rate = get_currency_rate(['USDBYR', 'RUBBYR', 'EURBYR', 'BYRBYR'])
    for row in csv.reader(file_table_with_data):
        row = row[:-1]
        table.append(row)
        try:
            if row[-1] in ['RUB', 'EUR', 'USD']:
                total_number_of_money_spent += int(row[3]) * currency_rate[row[-1]+'BYR']
            elif row[-1] == 'BYR':
                total_number_of_money_spent += int(row[3])
        except:
            print('server error')
    table = table[1:]
    table_t = list(zip(*table))
    pprint.pprint(table_t)
    pprint.pprint(currency_rate)
    pprint.pprint(total_number_of_money_spent)

if __name__ == "__main__":
    infile = open('car_stats.csv', 'rb')
    parsing_csv_file_and_total_number_of_money_spent(infile)
