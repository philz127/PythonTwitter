#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "cnn")
query2 = twitter.search.tweets(q = "fox news")
querry3 = twitter.search.tweets(q = "reuters")

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))
print("Search complete (%.3f seconds)" % (query2["search_metadata"]["completed_in"]))
print("Search complete (%.3f seconds)" % (query2["search_metadata"]["completed_in"]))

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))

for result in query2["statuses"]:
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
for result in query3["statuses"]:
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
