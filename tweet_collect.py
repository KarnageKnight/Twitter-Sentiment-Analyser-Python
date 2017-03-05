from threading import Thread
import time
import urllib
import twurl
import json
import sys

TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
word = raw_input('Enter word:')
word_no_retweet = word + ' -RT' #filter out no retweet
f = open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","a+")
count = 0
for x in range(0,3):   #range defines number of pages displayed
	if x==0:
		url = twurl.augment(TWITTER_URL, {'q': word_no_retweet, 'count': '100', 'lang': 'en', 'include_entities': 'false', 'return_type': 'popular'} ) #for first page
	else:
		url = twurl.augment(TWITTER_URL,{'q' : word_no_retweet, 'count': '100', 'lang': 'en', 'include_entities': 'false', 'max_id' : next_max_id, 'return_type': 'popular'}) #for subsequent tweets using their max_id
	#print 'Retrieving', url
	#print word_no_retweet
	print ''
	connection = urllib.urlopen(url) #create a connection to url 
	data = connection.read() #read whole page in a file format
	headers = connection.info().dict #store all headers and their values in data type dictionary 
    
	js = json.loads(data) #read data from a file type format and convert it to json format
	# print json.dumps(js,indent = 4)
	print 'Remaining', headers['x-rate-limit-remaining']
	print 'loop'
	for i in range(len(js['statuses'])):
		#print json.dumps(js, indent=4)
		next_max_id = str(json.dumps(js['statuses'][i]['id'])) #it is the next_max_id for the next result
   		f.write(json.dumps(js['statuses'][i]['text']))
   		f.write('\t')
   		if (json.dumps(js['statuses'][i]['user']['location'])=="\"\""):
   			f.write('None')
   		else:
   			f.write(json.dumps(js['statuses'][i]['user']['location']))
   		f.write('\n')
   	print next_max_id
f.close()
