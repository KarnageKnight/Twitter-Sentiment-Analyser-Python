from threading import Thread
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
	polarityData=json.loads(u.read()) #get polarity
	if(polarityData['label']=='pos'):
		polarity_file.write('positive\t')
		polarity_file.write(json.dumps(polarityData['probability']['pos'])) #write NLTK positive results to file
		polarity_file.write('\n') #new line
	elif(polarityData['label']=='neg'):
		polarity_file.write('negative\t')
		polarity_file.write(json.dumps(polarityData['probability']['neg'])) #write NLTK negative results to file
		polarity_file.write('\n') #new line
	else:
		polarity_file.write('neutraly\t')
		polarity_file.write(json.dumps(polarityData['probability']['neutral'])) #write NLTK neutral results to file
		polarity_file.write('\n') #new line
    
#TODO: Add retweet again

threadArray = [] #all the threads will be kept in this array, to be joined later
TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
word = raw_input('Enter word:')
word_no_retweet = word + ' -RT' #filter out no retweet
f = open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","a+")
count = 0
for x in range(0,3):   #range defines number of pages displayed
	if x==0:
		url = twurl.augment(TWITTER_URL, {'q': word_no_retweet, 'count': '100', 'lang': 'en', 'return_type': 'recent'} ) #for first page
	else:
		url = twurl.augment(TWITTER_URL,{'q' : word_no_retweet, 'count': '100', 'lang': 'en', 'include_entities': 'true', 'since_id' : next_max_id, 'return_type': 'recent'}) #for subsequent pages using their max_id
	#print 'Retrieving', url
	#print word_no_retweet
	print ''
	connection = urllib.urlopen(url) #create a connection to url 
	data = connection.read() #read whole page in a file format
	headers = connection.info().dict #store all headers and their values in data type dictionary 
    
	js = json.loads(data) #read data from a file type format and convert it to json format
	# print json.dumps(js,indent = 4)
	next_max_id = str(json.dumps(js['search_metadata']['max_id']-1)) #extract parameter next_results from search_metadata

	print 'Remaining', headers['x-rate-limit-remaining']
	print 'loop'

	for i in range(len(js['statuses'])):
		#print json.dumps(js, indent=4)
   		f.write(json.dumps(js['statuses'][i]['text'], indent=4))
   		f.write('\n')

	for i in range(len(js['statuses'])):    #loop through all the tweets on a page
		t = Thread(target=NLTK, args=(js, i, count,))
		threadArray.append(t)
		t.start()
	print 'NLTK running'
	for threadSingle in threadArray:    #join all threads before ending program
		try:
			threadSingle.join()
		except:
			print "Error: unable to join thread"

f.close()
   
