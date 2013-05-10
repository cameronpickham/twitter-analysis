from __future__ import division

import sys
import json
	
def main():
	words = open(sys.argv[1])
	tweets = open(sys.argv[2])
	word_scores = {}
	tweet_scores = {}
	tweet_text = []
	new_words = []

	# Create dictionary of terms and their scores
	for line in words:
		term, score = line.split("\t")
		word_scores[term] = int(score)

	# Load text of tweets into list
	for line in tweets:
		tweet = json.loads(line)
		if 'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))

	# For all tweets
	for t in tweet_text:
		sentiment = 0 # Initialize the tweet's sentiment to 0
		breakdown = t.split() # Split the tweet into individual strings
		
		# For every word in the tweet
		for word in breakdown:

			# If the word exists in argv[1], increase sentiment appropriately
			# Else, add it to the list of new words
			if word_scores.has_key(word):
				sentiment = sentiment + word_scores[word]
			else:
				new_words.append(word)

		tweet_scores[t] = int(sentiment)

	# For all new words
	for new in new_words:
		pos = neg = total = 0
		for t in tweet_scores:
			if new in t:
				if tweet_scores[t] > 0:
					pos+=1
				elif tweet_scores[t] < 0:
					neg+=1
				total+=1
		print new, ' ', (pos - neg)/total

if __name__ == '__main__':
    main()
