import sys
import json
import types
import operator

def main():
	tweets = open(sys.argv[1])
	hashtag_count = {}
	top = 10

	# Evaluate tweets
	for line in tweets:
		tweet = json.loads(line)
		if 'entities' in tweet and type(tweet['entities']) is not types.NoneType:
			if 'hashtags' in tweet['entities'] and type(tweet['entities']['hashtags']) is not types.NoneType:
				hashtags = tweet['entities']['hashtags']
				for hashtag in hashtags:
					tag = hashtag['text'].encode('utf-8')
					if hashtag_count.has_key(tag):
						hashtag_count[tag] += 1
					else:
						hashtag_count[tag] = 1

	# Compute top ten hashtags
	for x in range(top):
		print sorted(hashtag_count.items(), key=lambda x:x[1], reverse=True)[x][0], 
		print ' ',
		print float(sorted(hashtag_count.items(), key=lambda x:x[1], reverse=True)[x][1])

if __name__ == '__main__':
	main()
