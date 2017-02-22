import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

awer=list()
print ''
word = raw_input('Enter word:')
#word1 = '%23' + word
url = twurl.augment(TWITTER_URL, {'q': word, 'count': '20', 'lang': 'en'} )
print 'Retrieving', url
connection = urllib.urlopen(url)
data = connection.read()
headers = connection.info().dict
print 'Remaining', headers['x-rate-limit-remaining']
js = json.loads(data)
print json.dumps(js, indent=4)
for u in js['statuses']:
	awer.append(u['text'])
print awer	
for q in awer:
	try:
		print q
	except:
		continue
	