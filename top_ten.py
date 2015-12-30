'''
Write a Python script top_ten.py that computes the ten most frequently occurring hashtags from the data you gathered in Problem 1.

'''

import sys
import json
import operator

def updating_frequency(text, frequency):
    for word in text:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

def calculate_frequency(fp):
    frequency = {}
    total = 0.0
    for line in fp:
        tweet = json.loads(line)
        if 'entities' in tweet:
            if tweet['entities']['hashtags'] != []:
                text = []
                for tag in tweet['entities']['hashtags']:
                    text.append(tag['text'])
                total += len(tweet['entities']['hashtags'])
                updating_frequency(text, frequency)
    final_frequency = sorted(frequency.items(), key = operator.itemgetter(1))
    final_frequency = final_frequency[::-1]
    for item in final_frequency[:10]:
        print item[0], item[1]/total
        
def main():
    tweet_file = open(sys.argv[1])
    calculate_frequency(tweet_file)
   
if __name__ == '__main__':
    main()
