import sys
import json
import operator

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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

def calculate_single_tweet_sent(tweet, state, sentiments, states_score):
    total = 0
    tweet = tweet.split(' ')
    for word in tweet:
        if word in sentiments:
            total += sentiments[word]
    if state in  states_score:
        states_score[state] += total
    else:
        states_score[state] = total

def stream_sent(tweets, sentiments):
    text = ""
    score = 0
    states_score = {}
    for line in tweets:
        tweet = json.loads(line)
        if 'user' in tweet and 'text' in tweet:
            text = tweet['text']
            state = tweet['user']['location']
            if state != None and state in states.values():
                score = calculate_single_tweet_sent(text, state, sentiments, states_score)
    happiest_state = max(states_score.iteritems(), key = operator.itemgetter(1))[0]
    for key in states:
        if states[key] == happiest_state:
            print key
                
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
