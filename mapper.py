from threading import Thread
import time
import urllib
import twurl
import json
import sys
import geojson
import time
import os

def NLTK(line, area):
	polarity_file = open("/Users/karnageknight/Desktop/majorProject/Data/polarity_file.txt","a+")  #create and open a file handle to store NLTK results 
	data2 = urllib.urlencode({'text': str(line)})  #encode tweet in proper format for API call
	u = urllib.urlopen('http://text-processing.com/api/sentiment/', data2) #perform NLTK API call
	polarityData=json.loads(u.read()) #get polarity
	country = geojson.countryFinder(area,)

	#writing the mapper file for the reducer input
	if(polarityData['label']=='pos'):
		polarity_file.write(country)
		polarity_file.write('\tpositive\t')
		polarity_file.write(json.dumps(polarityData['probability']['pos'])) #write NLTK positive results to file
		polarity_file.write('\n') #new line
		#print '%s\tpositive\t%s' % (country,json.dumps(polarityData['probability']['pos']))
	elif(polarityData['label']=='neg'):
		polarity_file.write(country)
		polarity_file.write('\tnegative\t')
		polarity_file.write(json.dumps(polarityData['probability']['neg'])) #write NLTK negative results to file
		polarity_file.write('\n') #new line
		#print '%s\tpositive\t%s' % (country,json.dumps(polarityData['probability']['neg']))
	else:
		polarity_file.write(country)
		polarity_file.write('\tneutral \t')
		polarity_file.write(json.dumps(polarityData['probability']['neutral'])) #write NLTK neutral results to file
		polarity_file.write('\n') #new line
		#print '%s\tpositive\t%s' % (country,json.dumps(polarityData['probability']['neutral']))
if os.path.exists("~/Desktop/majorProject/Data/polarity_file.txt"):
    os.remove("~/Desktop/majorProject/Data/polarity_file.txt")
threadArray = [] #all the threads will be kept in this array, to be joined later

# for line in sys.stdin:    #loop through all the tweets on a page
# 	line = line.strip()
# 	t = Thread(target=NLTK, args=(line, ))
# 	threadArray.append(t)
# 	t.start()
sleep_count=0
with open("/users/karnageknight/Desktop/majorProject/Data/search_result.txt","r+") as f:
    for line in f:
    	line = line.strip()
    	getPolarity = line.split('\t',2)
    	t = Thread(target=NLTK, args=(getPolarity[0], getPolarity[1],))
    	threadArray.append(t)
    	t.start()
    	sleep_count+=1
    	if sleep_count%10==0:
    		time.sleep(2)
    	

for threadSingle in threadArray:    #join all threads before ending program
	try:
		threadSingle.join()
	except:
		print "Error: unable to join thread"