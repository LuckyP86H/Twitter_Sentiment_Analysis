import sys
import json

def updating_frequency(text, frequency):
    total = 0
    text = text.split(' ')
    for word in text:
        word = word.replace('\n', ' ')
        if word != " ":
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
            total += 1
    return total

def calculate_frequency(fp):
    frequency = {}
    total = 0.0
    for line in fp:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text']
            total += updating_frequency(text, frequency)
    #print total
    for key, value in frequency.iteritems():
        print key, float(value/total)
        #print key.strip('\n'), float(float(frequency[key]) / float(total))#, float(frequency[key] / total)
    #print total

def main():
    tweet_file = open(sys.argv[1])
    calculate_frequency(tweet_file)
   
if __name__ == '__main__':
    main()
