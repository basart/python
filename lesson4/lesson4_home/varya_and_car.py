# -*- coding:utf8 -*-
import csv
import urllib2
import json
import re
import pprint


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


def make_list_in_tuple_list_in_list(list_tuple):
    for column in range(len(list_tuple)):
        list_tuple[column] = list(list_tuple[column])
    return list_tuple


def formatting_table(table_with_data):
    number_row_in_table = len(table_with_data[0])
    currency_rate = get_currency_rate(['USDBYR', 'RUBBYR', 'EURBYR', 'BYRBYR'])
    for index_row in range(number_row_in_table):
        table_with_data[2][index_row] = float(table_with_data[2][index_row])
        try:
            if table_with_data[5][index_row] in ['RUB', 'EUR', 'USD']:
                table_with_data[3][index_row] = int(table_with_data[3][index_row]) * currency_rate[table_with_data[5][index_row]+'BYR']
            elif table_with_data[5][index_row] == 'BYR':
                table_with_data[3][index_row] = int(table_with_data[3][index_row])
        except:
            print('server error 111')
    # pprint.pprint(table_with_data)
    return table_with_data


def parsing_csv_file_and_total_money_spent(file_table_with_data):
    # table = [row[:-1] for row in csv.reader(infile)]
    table = []
    for row in csv.reader(file_table_with_data):
        row = row[:-1]
        if row[0]:
            table.append(row)
    table = table[1:]
    table_t = list(zip(*table))
    table_t = make_list_in_tuple_list_in_list(table_t)
    formatting_table_t_data = formatting_table(table_t)
    return formatting_table_t_data


def get_total_money_spent(tupple_money):
    total_number_of_money_spent = 0.0
    for day_information in tupple_money:
        total_number_of_money_spent += day_information
    return total_number_of_money_spent


def average_fuel_consumption(total_mileage, list_of_fuel_day, calculation_of_the=100):
    average_fuel_consumption_of_the = (sum(list_of_fuel_day) - 13.6 - list_of_fuel_day[-1]) / total_mileage * calculation_of_the
    return average_fuel_consumption_of_the


def get_month_and_year(date):
    day = ''
    day = day.join(re.findall('\/\w+\/', date))
    month_and_year = date.replace(day, '')
    return month_and_year


def get_count_month(list_date_day):
    month = set()
    for day_information in range(len(list_date_day)):
        month.add(get_month_and_year(list_date_day[day_information]))
    count_month = len(month)
    return count_month


if __name__ == "__main__":
    infile = open('car_stats.csv', 'rb')
    transposed_data_table = parsing_csv_file_and_total_money_spent(infile)
    total_money_spent = get_total_money_spent(transposed_data_table[3])
    average_fuel_consumption_on_100_km = average_fuel_consumption(
        int(transposed_data_table[1][-1]), transposed_data_table[2])
    average_cost_for_total_month = total_money_spent / get_count_month(transposed_data_table[0])
    print('Всего денег потрачено на топливо - %.2f р.' % total_money_spent)
    print('В среднем в месяц уходит в денег на топливо - %.2f р.' % average_cost_for_total_month)
    print('Средний расход топлива, в литрах на 100 км - %.5f л' % average_fuel_consumption_on_100_km)
