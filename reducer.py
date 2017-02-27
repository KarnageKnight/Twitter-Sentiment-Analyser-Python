#!/usr/bin/python
from operator import itemgetter
import sys

total_count=0
for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t',1)
	count = float(count)
	if word == 'positive':	
		total_count = total_count+count
	elif word == 'negative':
		total_count = total_count-count

final_file = open("/Users/karnageknight/Desktop/majorProject/Data/final_file.txt","w+")

if total_count > 0:
	final_file.write('positive\t')
	final_file.write(str(total_count))
	print 'positive\t%s' % (total_count)
else:
	final_file.write('negative\t')
	final_file.write(str(total_count*-1))
	print 'negative\t%s' % (total_count*-1)

final_file.close()
