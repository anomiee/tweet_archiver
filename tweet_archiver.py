#!/usr/bin/env python
# encoding: utf-8

import sys
try:
	import savepagenow
except ImportError:
	print "You'll need the savepagenow python2 module installed"
	sys.exit()
try:
	import archiveis
except ImportError:
	print "You'll need the archiveis python2 module installed"
	sys.exit()
try:
        import tweepy #https://github.com/tweepy/tweepy
except ImportError:
	print "You'll need tweepy installed on your system."
	sys.exit()

# EDIT THIS!
#Twitter API credentials - https://apps.twitter.com/
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):

	if (consumer_key == ""):
		print "You need to set up the script first. Edit it and add your keys."
		return

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before {0}".format(oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,include_entities = True, tweet_mode = 'extended')
		
				
		#save most recent tweets
		alltweets.extend(new_tweets)

				
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
				
		print "...{0} tweets downloaded so far".format(len(alltweets))
		
		for tweet in alltweets:
			tweetID=tweet.id_str
			tweetURL="https://twitter.com/{0}/status/{1}".format(screen_name,tweetID)
			
			print "Archiving {0}...".format(tweetURL)
			archive_url = archiveis.capture(tweetURL)
			archiveorg_url = savepagenow.capture_or_cache(tweetURL)
			print "Tweet archived! archive.is: {0} ||| archive.org: {1}".format(archive_url,archiveorg_url[0])
	
		print "All tweets successfully archived."

if __name__ == '__main__':
	if (len(sys.argv) == 2):
		get_all_tweets(sys.argv[1])
	else:
		print "Please add the twitter account you want to back up as an argument."
