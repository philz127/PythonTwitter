#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------
import datetime
from twitter import *
import re

import csv


#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys



#-----------------------------------------------------------------------
# create twitter streaming API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth("1049316523981119488-m6XsMMlmDJbderLe8yj2HeDsqHzd3w",
                               "pKHH0Ys2ldp3kwUTgBI85Ons9GY0zw5qDrwsNuCbSer91",
                               "1hJjet2v0EaR4wFf0tzwx5AhY",
                               "4M4l6ZDb68s8fVOEI3zb2vIWE0D4IZdW0mda5ZZ7PI9mgD1Q9j"))
date = datetime.datetime.now().strftime("%Y-%m-%d")
outfile = "Tweets_ALL_NEWS" + date + ".csv"

#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import csv

csvfile = open(outfile, "w")
csvwriter = csv.writer(csvfile)

row = ["created","user","text"]
csvwriter.writerow(row)
#-----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------

query = twitter.search.tweets(q = "Fox%20News%20OR%20npr%20OR%20cnn%20reuters", count = 200)
#query = twitter.search.tweets(q = "Fox%20News%20OR%20npr%20OR%20cnn%20reuters", count = 200, since ='2019-02-21', until= date )


#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
    user = result["user"]["screen_name"]
    text = result["text"]
    created = result["created_at"]
    text = text.encode('ascii', 'replace')
    row = [created, user, text]
    csvwriter.writerow(row)
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))
csvfile.close()
print("done")
