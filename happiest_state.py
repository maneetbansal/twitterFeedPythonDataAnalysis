'''
Created on May 14, 2013

@author: maneet
'''
import json
import sys
import re

# this script gives the happiest state on the basis of tweet sentiment score calculated by "tweet_sentiment.py"

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
def wordSplitForTweetText(tweetText):
    nonalpha = re.compile(r'[^a-z]+')
    tokens = nonalpha.split(tweetText.lower())
    return tokens

def readSentFileToDictionary(fp):
    afinnfile = open(fp)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def main():
    
    afinnFileDict = readSentFileToDictionary(sys.argv[1])
    #afinnFileDict = readSentFileToDictionary("AFINN-111.txt")
    tweet_file_fp = open(sys.argv[2])
    #tweet_file_fp = open("part3.txt")
    
    stateScoredict = {}
    for line in tweet_file_fp:
        a_dict = json.loads(line)
    #print a_dict.keys()
        if(a_dict.has_key('place')):
            if(a_dict['place']):
                if(a_dict['place'].has_key('country') and a_dict['place'].has_key('full_name')):
                    if a_dict['place']['country'] == "United States":
                        if states.has_key(a_dict['place']['full_name'].split()[1]):
                            stateCode = a_dict['place']['full_name'].split()[1]
                            stateScoredict[stateCode] = 0.0
                            tweet_dict = json.loads(line)
                            if "text" in tweet_dict:
                                strArray = wordSplitForTweetText(tweet_dict['text'])
                                outputScore = 0
                                for tweetWord in strArray:
                                    if(tweetWord):
                                        if afinnFileDict.has_key(tweetWord):
                                            outputScore = outputScore + afinnFileDict[tweetWord]
                                
                                stateScoredict[stateCode] =  stateScoredict[stateCode] + outputScore
                                               
                                        
    sortedlist = sorted(stateScoredict, key=stateScoredict.get, reverse=True)
    print sortedlist[0]
    
   
if __name__ == '__main__':
   main()
