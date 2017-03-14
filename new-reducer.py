#!/usr/bin/python
from operator import itemgetter
import sys
import os

if os.path.exists("~/Desktop/majorProject/Data/final_file.txt"):
    os.remove("~/Desktop/majorProject/Data/final_file.txt")
total_count=0 	#overall polarity
current_country = None 
country_count = 0	#country polarity
country_number = 1 #number of tweets per country
total_tweets=0 #number of total tweets
final_file = open("/Users/karnageknight/Desktop/majorProject/Data/final_file.txt","a+")

# with open("/users/karnageknight/Desktop/majorProject/Data/polarity_file.txt","r+") as f:
# 	for line in f:
for line in sys.stdin:
	line = line.strip()
	country, word, count = line.split('\t',3)
	count = float(count)
	if word == 'positive':	
		if current_country == country:
			country_count += count        #update count of current country
			country_number=country_number+1 #one added for every tweet of the same country checked, be it pos, neg or neutral
		else:
			if current_country:			#if current country is not equal country and is not None 
				final_file.write(current_country)
				final_file.write('\t')
				final_file.write(str(country_count))
				final_file.write('\t')
				final_file.write(str(country_number))
				final_file.write('\n') #write current country and country count to file 
			country_count=count		
			current_country=country	#change current country
			total_tweets+=country_number
			country_number=1 #reset after every country
		total_count = total_count+count
	elif word == 'negative':
		if current_country == country:	
			country_count -= count
			country_number+=1 #one added for every tweet of the same country checked, be it pos, neg or neutral
		else:
			if current_country:       #if current country is not equal country and is not None 
				final_file.write(current_country)
				final_file.write('\t')
				final_file.write(str(country_count))
				final_file.write('\t')
				final_file.write(str(country_number))
				final_file.write('\n')   #write current country and country count to file 
			country_count=count
			current_country=country  #change current country
			total_tweets+=country_number
			country_number=1 #reset after every country
		total_count = total_count-count
	elif word == 'neutral ':
		if current_country==country:
			country_number+=1 #one added for every tweet of the same country checked, be it pos, neg or neutral
		else:
			country_number=1 #reset after every country

if current_country == country:
	print '%s\t%s' % (current_country, country_count)
	final_file.write(current_country)
	final_file.write('\t')
	final_file.write(str(country_count))
	final_file.write('\t')
	final_file.write(str(country_number))
	final_file.write('\n')   #write current country and country count to file 


if total_count > 0:
	final_file.write('Total positive:\t')
	final_file.write(str(total_count))
	final_file.write('\tTotal Tweets:\t')
	final_file.write(str(total_tweets))
	print 'Total positive:\t%s' % (total_count)
else:
	final_file.write('Total negative:\t')
	final_file.write(str(total_count*-1))
	final_file.write('\tTotal Tweets:\t')
	final_file.write(str(total_tweets))
	print 'Total negative:\t%s' % (total_count*-1)

final_file.close()