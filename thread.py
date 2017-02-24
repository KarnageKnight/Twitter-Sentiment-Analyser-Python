import thread
import time
import urllib
import twurl
import json


# Define a function for the thread
def NLTK(js, i, count):
   	count += 1
	polarity_file = open("/Users/karnageknight/Desktop/majorProject/Data/polarity_file.txt","a+")  #create and open a file handle to store NLTK results 
	tweet = json.dumps(js['statuses'][i]['text'], indent=4)
	data2 = urllib.urlencode({'text': str(tweet)})  #encode tweet in proper format for API call
	u = urllib.urlopen('http://text-processing.com/api/sentiment/', data2) #perform NLTK API call
	polarity_file.write(u.read()) #write NLTK results to file
	polarity_file.write('\n') #new line 
    


   
TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
word = raw_input('Enter word:')
word_no_retweet = word + ' -RT' #filter out no retweet
f = open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","a+")
count = 0
for x in range(0,3):   #range defines number of pages displayed
	if x==0:
		url = twurl.augment(TWITTER_URL, {'q': word_no_retweet, 'count': '100', 'lang': 'en'} ) #for first page
	else:
		url = twurl.augment(TWITTER_URL,{'q' : word_no_retweet, 'count': '100', 'lang': 'en', 'include_entities': 'true', 'max_id' : next_max_id}) #for subsequent pages using their max_id
	#print 'Retrieving', url
	#print word_no_retweet
	print ''
	connection = urllib.urlopen(url) #create a connection to url 
	data = connection.read() #read whole page in a file format
	headers = connection.info().dict #store all headers and their values in data type dictionary 
    
	js = json.loads(data) #read data from a file type format and convert it to json format
	try:
		next_results_url_params = js['search_metadata']['next_results'] #extract parameter next_results from search_metadata
		next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0] #extract max_id of next page from next_results
	except:
        # No more next pages
		break

	print 'Remaining', headers['x-rate-limit-remaining']
	print 'loop'

	for i in range(len(js['statuses'])):
		#print json.dumps(js, indent=4)
   		f.write(json.dumps(js['statuses'][i]['text'], indent=4))
   		f.write('\n')


	for i in range(len(js['statuses'])):    #loop through all the tweets on a page
		try:
			thread.start_new_thread( NLTK, (js, i, count) )
		except:
			print "Error: unable to start thread"

f.close()
   
