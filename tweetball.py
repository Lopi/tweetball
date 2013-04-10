## tweetball.py
#!/usr/bin/env python
 
import json
import urllib2
import sys
 
def banner():
        print '''                                                                  
                                      O.                                      
                                     OOO                                      
                                   ZOOOOOO                                    
                                 :OOOOOOOOO~                                  
                               :OOOOOOOOOOOOOZ                                
          OO..               OOOOOOOOOOOOOOOOOOO..               OO            
          8OOOOOO.     .OOOOOO8OOOOOOO.    O O8OOOO8O.     .8OOOOOO            
          OOOOOOOOOOOOOOOOO8OOOOOOOO    OO.  .OOOOO8OOOOOOOOOOOOOOO            
          OOOOOO 8OOOOOOOO+OOO8OOO    OO      OOOOO$O8OOOOOO$OOOOOO            
          OOOOO. O88OOOOO. OOOOOO   O8+       OOOO  OOOO8OOO  OOOOO            
          OOOO    OOOOOO    OOOO   OO. .      O8O   .8OOOOO   .OOO8            
          OOOO. . OOOOOO  ..OOO  .O  O        OOO .  OOOOOO    OOOO            
          OOOOOOOO$OOOOOO8OO.OO   I.O        OOO.OOOOOOOOO=OOOO8OOO            
          OOOOOO$OOOOOOOOOOO8OO  .I         .OOOOOOOOOOOOOOOOOOOOOO            
          OOOOOO OOOOOOOO..OOOO  O          OOOOOOI OOOOOOOO  OOOO8            
          OO8.     .OOO.     OO..        .OOOOOO     .+OOO      OOO            
          OOOOO   O8OOOO.  .OOO,O       8OOO8OOO8.  .OOOOOO    OOOO            
          OOOO OO.OOOOOO.OO.OO8OO   .OOOOOOOOOOOO OO.OOOOOO.OO 8OOO            
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO8OOOOOOO8OOO            
          OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO            
          OOO                                                   OOO            
          OOO   Z$$Z$Z   Z$Z$Z$$$.$Z$ZZ$$ZZZ$ZZ $$$$$$Z$        OOO            
          OOO   $$Z$$$.  Z$Z$$$$$ ZZ$$$$Z$Z$Z$Z $Z$$Z$$$        OOO            
          OOO   $$Z$$ZZ   $Z$$$Z  $Z$Z$$$$$Z$$Z  ZZZZZZ.        OOO            
          OOO.    Z$$$$    $$$Z    :$Z$$   =$$$   $Z$$          OO8            
          OOO     ZZ$Z$$   $$$$    :$$Z$      .   Z$$$          OOO            
          OOO     $$ZZZ$   $$$$    :$ZZ$          $$$Z          OO8            
          OOO     $$$Z$ZZ  $$ZZ    :$ZZ$     .    $$$Z          OOO            
          OOO     $$$$Z$Z. $ZZZ    :$$$$  $ZZ     $ZZ$          OOO            
          OOO     $$$$$$$Z $$ZZ    :$$$Z$$$Z$     $Z$Z          OOO            
          OOO     $$Z$ZZ$$:$Z$Z    :$$$ZZ$$$Z     $$$$          OOO            
          O8O     $$$$ $$$$$$$$    :Z$Z$   $$     $$$Z          O8O            
          OOO     $$$Z $Z$$$$$$    :Z$$$          ZZ$$    $$$   OO8            
          OOO     $ZZ$  $$Z$$ZZ    :$$$Z          $$$$    $$Z   OOO            
          OOO     $$$$  7$$Z$$Z    :ZZ$$          $$Z$    Z$Z   OO8            
          OOO   $ZZ$$Z. .$$Z$$Z    :$$$Z          Z$$$..ZZZ$$   O8O            
          OOO   $$Z$Z$$. =$$$$$    :$$Z$         .Z$$Z$$ZZ$$$   OOO            
          ZOOO .Z$Z$$$$:  $$$ZZ    :Z$$Z        $$$$Z$$ZZZ$$   OO8O            
           OOOO        :  .$$$Z  .$$$Z$$        ZZ$Z$Z:      .OOOO            
            O8OO8.         ..$$   $Z$Z$ZZ       $.          OOOOO              
              O8OOOOO..           .$$$$$Z              .OOOOOOO.              
                OOOOOOOOOOOO         ..Z$.      .OOOO8OOOOOO=.                
                   .OOOOOOOOOOOOO.          OOOOOOOO8OOO..                    
                            ZOOOOOOO     ,OOOOOO                              
                                OOOOOI .OOOOZ                                  
                                  .OOOOO8O.                                    
                                    ZOOOO                                      
                                      O.                                      
'''                                                                    
       
 
        title = 'tweetball.py: Python script to scrape publicly available tweets during the 2012-2013 NFL Season'
        contact = 'chris.spehn@gmail.com'
       
        print '---------------------------------------------------------------------------------------------------'
        print title
        print 'contact: ' + contact
        print '---------------------------------------------------------------------------------------------------'
                   
 
def usage():
        print "You can't launch tweetball.py without a twitter name!"
        print "Usage: python tweetball.py twitter_name"
        print "Example: python tweetball.py _Lopi_"
 
# Date format: Wed Dec 05 20:49:21 +0000 2012
# NFL Football Season Date Range: Sep 01 2012 -- Feb 05 2013
import time
tweetMin = time.strptime("Sep 01 2012", "%b %d %Y") # <-- Edit these dates if you want to search a different time frame
tweetMax = time.strptime("Feb 05 2013", "%b %d %Y") # <-- Edit these dates if you want to search a different time frame
def compareDate(tweetDate):
    tweetDate = tweetDate.split()
    tweetDay = time.strptime(" ".join(tweetDate[1:3] + [tweetDate[-1]]), "%b %d %Y")
    return tweetMin <= tweetDay and tweetDay <= tweetMax
 
# Timeline request for 200 tweets, 3200 maximum
# Maximum of 150 requests an hour
# Timeline request: https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=_Lopi_&count=200
def getTimeline():
 
        tweet_id = 999999999999999999999999999
        screen_name = sys.argv[1]
        filename = screen_name + ".txt"
        count = 1
       
        print '[+] Starting to scrape tweets'
        print "[+] Sending request number " + str(count) + " to Twitter"
        req = urllib2.Request('https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + screen_name + '&count=200')
        response = urllib2.urlopen(req)
        print "[+] Receiving response from Twitter"
        the_page = response.read()
        print "[+] Parsing response from Twitter"
        tweets = json.loads(the_page)
        timeline = json.dumps(json.loads(the_page), indent=4, sort_keys=True)
 
        for tweet in tweets:
                tweetDate = tweet['created_at'].encode('utf-8')
                if compareDate(tweetDate) == 1:
                        the_tweets = tweet['text'].encode('utf-8') + "\n"
                        f = open(filename, 'a')
                        f.write(tweetDate + ": " + the_tweets)
                        f.close()
 
        for str_id in tweets:
                if tweet_id > str_id['id']:
                        tweet_id = str_id['id']
 
        print "[+] Smallest Tweet ID Found: " + str(tweet_id)
       
 
        print "[+] Writing tweets to file: " + filename
       
 
        while len(str(str_id['id'])) > 11:
                try:
                        count = count + 1
                        print "[+] Sending another request with max_id=" + str(tweet_id)
                        print "[+] Sending request number " + str(count) + " to Twitter"
                        req = urllib2.Request('https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=' + screen_name + '&count=200' + '&max_id=' + str(tweet_id))
                        response = urllib2.urlopen(req)
                        print "[+] Receiving response from Twitter"
                        the_page = response.read()
                        print "[+] Parsing response from Twitter"
                        tweets = json.loads(the_page)
                        timeline = json.dumps(json.loads(the_page), indent=4, sort_keys=True)
 
                        for tweet in tweets:
                                tweetDate = tweet['created_at'].encode('utf-8')
                                if compareDate(tweetDate) == 1:
                                        the_tweets = tweet['text'].encode('utf-8') + "\n"
                                        f = open(filename, 'a')
                                        f.write(tweetDate + ": " + the_tweets)
                                        f.close()
 
                        print "[+] Writing tweets to file: " + filename
               
                        for str_id in tweets:
                                if tweet_id > str_id['id']:
                                        tweet_id = str_id['id']
 
                        print "[+] Smallest Tweet ID Found: " + str(tweet_id)
 
 
 
                except:
                        sys.exit("[+] An unexpected error occurred")
 
def main():
        banner()
        getTimeline()
 
if __name__ == '__main__':
    if len(sys.argv) <> 2:
        usage()
        sys.exit(1)
    else:
        main()