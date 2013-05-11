from __future__ import division
import sys
import json

def main():
	tweets = open(sys.argv[1])
	term_dict = {}
	term_total = 0

	# Load terms into dictionary mapping (term, count)
	for line in tweets:
		tweet = json.loads(line)
		if 'text' in tweet:
			terms = tweet['text'].lower().encode('utf-8').split()
			for term in terms:
				if term_dict.has_key(term):
					term_dict[term] = term_dict[term] + 1
				else:
					term_dict[term] = 1
				term_total += 1

	# Print dictionary
	for x in term_dict:
		print x, ' ', term_dict[x]/term_total

if __name__ == '__main__':
    main()
