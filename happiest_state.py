import sys
import json
import types

def main():
	words = open(sys.argv[1])
	tweets = open(sys.argv[2])
	scores = {}
	state_scores = {}

	# Create dictionary mapping (term, score)
	for line in words:
		term, score = line.split("\t")
		scores[term] = int(score)

	# Evaluate tweets
	for line in tweets:
		sentiment = 0
		tweet = json.loads(line)
		if 'text' in tweet:
			terms = tweet['text'].lower().encode('utf-8').split()
			for term in terms:
				if scores.has_key(term):
					sentiment = sentiment + scores[term]
		if 'place' in tweet and type(tweet['place']) is not types.NoneType:
			if 'full_name' in tweet['place'] and type(tweet['place']['full_name']) is not types.NoneType:
				if 'country_code' in tweet['place'] and type(tweet['place']['country']) is not types.NoneType:
					if tweet['place']['country'] == 'United States':
						name_line = tweet['place']['full_name'].encode('utf-8')
						details = name_line.split()
						state = details[-1]
						if len(state) == 2:
							if state_scores.has_key(state):
								state_scores[state] = state_scores[state] + sentiment
							else:
								state_scores[state] = sentiment

	happiest_state = state_scores.keys()[0]
	for state in state_scores:
		if state_scores[state] > state_scores[happiest_state]:
			happiest_state = state
	print happiest_state

if __name__ == '__main__':
	main()
