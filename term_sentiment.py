'''
Created on May 14, 2013

@author: maneet
'''
import sys
import json


#on the basis of the tweer of given sentiment, sentiments of the words in the tweet has been calculated using this script.

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def readFileToDictionary(fp):
    afinnfile = open(fp)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def readTweetFromFile(fp):
    sampleFile = open(fp)
    outputList = []
    for line in sampleFile:
        a_dict = json.loads(line)
        if "text" in a_dict:
            outputList.append(a_dict['text'])

    return outputList  
#print scores.items() # Print every (term, score) pair in the dictionary 

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
    #sent_file = "AFINN-111.txt"
    #tweet_file = "part1.txt"
    afinnFileDict = readFileToDictionary(sys.argv[1])
    tweetList = readTweetFromFile(sys.argv[2])
  #  print tweetList
    tweetSentimentDict = {}
    outputDict = {}
   # positiveNegativeArray = [0.0,1.0];
    for tweet in tweetList:
        strArray = tweet.split(" ")
        outputScore = 0
        
        for tweetWord in strArray:
            if(tweetWord):
                if afinnFileDict.has_key(tweetWord):
                    outputScore = outputScore + afinnFileDict[tweetWord]
                else:
                    outputDict[tweetWord] = 0.0
        tweetSentimentDict[tweet] = outputScore
        
    # Checking the score of tweet containing the word. If positive increasing the postive part else increasing the negative part
    
    for word in outputDict:
        posValue = 0.0
        negValue = 1.0
        for tweet in tweetSentimentDict:
            strArray = tweet.split(" ")
            if word in strArray:
                if tweetSentimentDict[tweet] >= 0:
                    posValue +=1 #outputDict[word][0] +1;
                else:
                    negValue +=1
#         print word
#         print posValue
#         print negValue
#         print
        
        outputDict[word] = posValue/negValue
#     print "-----------"
    for entry in outputDict:     
        print entry,round(outputDict[entry], 5)




if __name__ == '__main__':
   main()

      
