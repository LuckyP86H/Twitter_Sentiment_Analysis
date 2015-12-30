import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def create_sent_dictionary(afinnfile):
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def calculate_single_tweet_sent(tweet, sentiments):
    total = 0
    tweet = tweet.split(' ')
    for word in tweet:
        if word in sentiments:
            total += sentiments[word]
    return total

def stream_sent(tweets, sentiments):
    text = ""
    score = 0
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text']
            score = calculate_single_tweet_sent(text, sentiments)
        print score

def main():
    sent_file = open(sys.argv[1])
    sent_file2 = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet_file2 = open(sys.argv[2])
    sentiments = create_sent_dictionary(sent_file2)
    #hw()
    stream_sent(tweet_file2, sentiments)
   
if __name__ == '__main__':
    main()
