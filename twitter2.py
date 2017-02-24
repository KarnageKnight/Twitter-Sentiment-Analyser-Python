import urllib
import twurl
import json
import threading
import itertools

def NTLK (i) :
	g = open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","r+")
	lines = g.readlines()
	line_number=1
	polarity_file = open("/users/karnageknight/Desktop/majorProject/Data/polarity_file.txt","a+")
	with open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt", 'r') as datafile:
		for line in itertools.islice(datafile ,i, i+1):
			data2 = urllib.urlencode({'text': line})
			u = urllib.urlopen('http://text-processing.com/api/sentiment/', data2)
			print data2
			polarity_file.write(u.read())
			polarity_file.write('\n')
			print 'line=',i
			line_number=line_number+1
	polarity_file.close()
	g.close()
	try:
		t.exit()
	except:
		print 'ho gya'

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
word = raw_input('Enter word:')
count=0
word_no_retweet = word + ' -RT'
f = open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","a+")
for x in range(0,3):
	if x==0:
		url = twurl.augment(TWITTER_URL, {'q': word_no_retweet, 'count': '100', 'lang': 'en'} )
	else:
		url = twurl.augment(TWITTER_URL,{'q' : word_no_retweet, 'count': '100', 'lang': 'en', 'include_entities': 'true', 'max_id' : next_max_id})
	print 'Retrieving', url
	#print word_no_retweet
	print ''
	connection = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
    
	js = json.loads(data)
	try:
		next_results_url_params = js['search_metadata']['next_results']
		next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
	except:
        # No more next pages
		break

	for i in range(len(js['statuses'])):
		#print json.dumps(js, indent=4)
   		f.write(json.dumps(js['statuses'][i]['text'], indent=4))
   		f.write('\n')
		count+=1

	print 'Remaining', headers['x-rate-limit-remaining']
	print 'count = ', count
	
	#for i in range(100):
	#	try:
	#		t = threading.Thread(target=NTLK, args=(i,))
	#		t.start()
	#	except:
	#		print 'Thread exception'
	#		continue

f.close()




