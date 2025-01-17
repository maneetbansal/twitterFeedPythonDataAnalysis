import sys
import json

#this script calculates the sentiment of all the tweets given in an input file. To compute the sentiments "AFINN-111.txt" file is used whoch #contains precomputed sentiments of some of the words.

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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    #sent_file = "AFINN-111.txt"
    #tweet_file = "part1.txt"
    afinnFileDict = readFileToDictionary(sys.argv[1])
    tweetList = readTweetFromFile(sys.argv[2])
  #  print tweetList
    for tweet in tweetList:
        strArray = tweet.split(" ")
        outputScore = 0
        
        for tweetWord in strArray:
            if afinnFileDict.has_key(tweetWord):
                outputScore = outputScore + afinnFileDict[tweetWord]
        print outputScore
            
   # hw()
   # lines(sent_file)
   # lines(tweet_file)



if __name__ == '__main__':
   main()

   
