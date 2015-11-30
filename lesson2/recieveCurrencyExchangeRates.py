import urllib2
import json
import pprint

s = 'https://query.yahooapis.com/v1/public/yql?q=select+*+from+yahoo.finance.xchange+where+pair+=+%22USDRUB,EURRUB%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
u = urllib2.urlopen(s)
                            #print u.getcode()
data = u.read()
                            #print data
parsed_data = json.loads(data)
#pprint.pprint(parsed_data)
print parsed_data.keys()
print parsed_data["query"]["results"]
print parsed_data['query']['results']['rate'][0]['Rate']
print parsed_data['query']['results']['rate'][1]['Rate']

for item in parsed_data['query']['results']['rate']:
    print ('{0} : {1}'.format(item['Name'], item['Rate']))

