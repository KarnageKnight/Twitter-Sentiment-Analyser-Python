#!/usr/bin/python
from operator import itemgetter

total_count=0
with open("/Users/karnageknight/Desktop/majorProject/Data/polarity_file.txt","r+") as polarity_file:
	for line in polarity_file:
		line = line.strip()
		word, count = line.split('\t',1)
		count = float(count)
		if word == 'positive':	
			total_count = total_count+count
		elif word == 'negative':
			total_count = total_count-count

	final_file = open("/Users/karnageknight/Desktop/majorProject/Data/final_file.txt","w+")

	if total_count > 0:
		print '%s\t%s' % ('positive',total_count)
		final_file.write('positive\t')
		final_file.write(str(total_count))
	else:
		print '%s\t%s' % ('negative',(total_count*(-1)))
		final_file.write('negative\t')
		final_file.write(str(total_count*-1))

	final_file.close()
