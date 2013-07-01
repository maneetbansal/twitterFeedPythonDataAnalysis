'''
Created on May 14, 2013

@author: maneet
'''
import json
import sys
import re

#This script generates the frequecy of the terms in the twitter feed, collected by "twitterstream.py"
 
#The frequency of a term can be calculate with the following formula:
[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

def wordSplitForTweetText(tweetText):
    nonalpha = re.compile(r'[^a-z]+')
    tokens = nonalpha.split(tweetText.lower())
    return tokens

def readTweetFromFile(fp):
    sampleFile = open(fp)
    outputList = []
    for line in sampleFile:
        a_dict = json.loads(line)
        if "text" in a_dict:
            outputList.append(a_dict['text'])

    return outputList 
def main():
    tweetList = readTweetFromFile(sys.argv[1])
    #tweetList = readTweetFromFile("part2.txt")
    wordOccurDict = {}
    for tweet in tweetList:
        strArray = wordSplitForTweetText(tweet)
        for tweetWord in strArray:
            if(tweetWord):
                if wordOccurDict.has_key(tweetWord):
                    wordOccurDict[tweetWord] +=1
                else:
                    wordOccurDict[tweetWord] =1.0
        
    total = 0.0
    for entry in wordOccurDict:
        if(entry):
            total = total + wordOccurDict[entry]
    
    for entry in wordOccurDict:
        if(entry):
            if(wordOccurDict[entry]):
                print entry,round(wordOccurDict[entry]/total, 3)
        else:
            continue
if __name__ == '__main__':
   main()
