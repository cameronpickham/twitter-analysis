import sys
import json

def main():
	words = open(sys.argv[1])
    	tweets = open(sys.argv[2])
	scores = {}
	tweet_text = []

	# Create dictionary of terms and their scores
	for line in words:
    		term, score = line.split("\t")
    		scores[term] = int(score)

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
    			if scores.has_key(word):
    				sentiment = sentiment + scores[word]
    		print sentiment


if __name__ == '__main__':
    main()
