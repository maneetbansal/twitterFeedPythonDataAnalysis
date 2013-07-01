'''
Created on May 15, 2013

@author: maneet
'''
import json
import sys

#this scipt is used to genearte top ten hash tags in collected tweeter stream


def main():
    tweet_file_fp = open(sys.argv[1])
    hashTagCountDict = {}
    #tweet_file_fp = open("part1.txt")
    for line in tweet_file_fp:
        a_dict = json.loads(line)
        if(a_dict.has_key('entities')):
            if(a_dict['entities'].has_key('hashtags')):
                for tag in a_dict['entities']['hashtags']:
                    if tag.has_key('text'):
                        if(hashTagCountDict.has_key(tag['text'])):
                            hashTagCountDict[tag['text']] +=1
                        else:
                            hashTagCountDict[tag['text']] = 1.0
    sortedlist = sorted(hashTagCountDict, key=hashTagCountDict.get, reverse=True)
    print sortedlist[0],hashTagCountDict[sortedlist[0]]
    print sortedlist[1],hashTagCountDict[sortedlist[1]]
    print sortedlist[2],hashTagCountDict[sortedlist[2]]
    print sortedlist[3],hashTagCountDict[sortedlist[3]]
    print sortedlist[4],hashTagCountDict[sortedlist[4]]
    print sortedlist[5],hashTagCountDict[sortedlist[5]]
    print sortedlist[6],hashTagCountDict[sortedlist[6]]
    print sortedlist[7],hashTagCountDict[sortedlist[7]]
    print sortedlist[8],hashTagCountDict[sortedlist[8]]
    print sortedlist[9],hashTagCountDict[sortedlist[9]]
            
                
                







if __name__ == '__main__':
   main()
