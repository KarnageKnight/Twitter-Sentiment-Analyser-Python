#!/usr/bin/python
from operator import itemgetter


total_positive = 0
total_negative = 0
total_neutral = 0
total_tweets = 0
data_rep=open('/Users/karnageknight/Desktop/majorProject/Data/data_rep.txt','a+')
data_rep.write ('country\t\t\t\tSkew Bar\t\t\tpos\tneg\tPolarity\n\n')
with open("/Users/karnageknight/Desktop/majorProject/Data/final_file.txt","r+") as final_file:
	for line in final_file:
		line=line.strip()
		country, polarity, pos, neg, neu, total = line.split('\t',6)
		total_positive+=int(pos)
		total_negative+=int(neg)
		total_neutral+=int(neu)
		total_tweets+=int(total)
		data_rep.write(str(country))
		if len(str(country))<8:
			data_rep.write('\t\t')
		else:	
			data_rep.write('\t')
		pos_percentage = float(pos)/float(total) *100
		neg_percentage = float(neg)/float(total) *100
		pos_bar_len = int(pos_percentage/5)
		neg_bar_len = int(neg_percentage/5)
		pos_bar = list('--------------------')
		neg_bar = list('--------------------')
		for i in range(pos_bar_len):
			pos_bar[i]='*'
		for i in range(neg_bar_len):
			neg_bar[19-i] = '*'
		data_rep.write("".join(neg_bar))
		data_rep.write('|')
		data_rep.write("".join(pos_bar))
		data_rep.write('\t')
		data_rep.write(str('%.2f' % (pos_percentage)))
		data_rep.write('\t')
		data_rep.write(str('%.2f' % (neg_percentage)))
		data_rep.write('\t')
		data_rep.write(str('%.2f' % (float(polarity)/float(total_tweets))))
		data_rep.write('\n')
data_rep.write('\n')
data_rep.write('\n')
data_rep.write('\n')
data_rep.write('total Positive tweets: ')
data_rep.write(str(total_positive))
data_rep.write('\t')
data_rep.write('total Negative tweets: ')
data_rep.write(str(total_negative))
data_rep.write('\t')
data_rep.write('total Neutral tweets: ')
data_rep.write(str(total_neutral))
data_rep.write('\t')
data_rep.write('total tweets: ')
data_rep.write(str(total_tweets))
data_rep.close()

