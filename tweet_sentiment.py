import sys
import json

def main():
  words = open(sys.argv[1])
  tweets = open(sys.argv[2])
  scores = {}
  tweet_text = []

  for line in words:
    term, score = line.split("\t")
    scores[term] = int(score)
    
  for line in tweets:
    tweet = json.loads(line)
    if 'text' in tweet:
      text = tweet['text'].lower()
      tweet_text.append(text.encode('utf-8'))

    for t in tweet_text:
      sentiment = 0
      breakdown = t.split()
    
      for word in breakdown:
        if scores.has_key(word):
          sentiment = sentiment + scores[word]
      
      print sentiment

if __name__ == '__main__':
    main()
