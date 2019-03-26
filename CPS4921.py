#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-stream-format:
#  - ultra-real-time stream of twitter's public timeline.
#    does some fancy output formatting.
#-----------------------------------------------------------------------
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


import datetime
from twitter import *
import re

import csv


#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys


date = datetime.datetime.now().strftime("%Y-%m-%d")
json_key = json.load(open('cred.json'))
scope = scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive',
         ]
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

sheetID = "1GafmIDcts7vFrZukvGy5dSnRCmPs-lvOtLoRl4z7AsQ"

file = gspread.authorize(credentials) 	
# authenticate with Google
#worksheet = sh.add_worksheet(title="Tweets_ALL_NEWS" + date, rows="200", cols="3")
#sheet = file.create("Tweets_ALL_NEWS"	).sheet1

sheet = file.open_by_key('1GafmIDcts7vFrZukvGy5dSnRCmPs-lvOtLoRl4z7AsQ').sheet1	
#	sheet = spreadsheet.add_worksheet(title="Tweets"+date, rows="100", cols="3")
#spreadsheet = file.open("Tweets_ALL_NEWS" + date) # open sheet

#-----------------------------------------------------------------------
# create twitter streaming API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth("1049316523981119488-m6XsMMlmDJbderLe8yj2HeDsqHzd3w",
                               "pKHH0Ys2ldp3kwUTgBI85Ons9GY0zw5qDrwsNuCbSer91",
                               "1hJjet2v0EaR4wFf0tzwx5AhY",
                               "4M4l6ZDb68s8fVOEI3zb2vIWE0D4IZdW0mda5ZZ7PI9mgD1Q9j"))

outfile = "Tweets_ALL_NEWS" + date + ".csv"


#-----------------------------------------------------------------------
import sys
sys.path.append(".")
#import csv

#csvfile = open(outfile, "w")
#csvwriter = csv.writer(csvfile)

row = [["created","user","text"]]
#csvwriter.writerow(row)
#-----------------------------------------------------------------------
# perform a basic search
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------

query = twitter.search.tweets(q = "Fox%20News%20OR%20npr%20OR%20cnn%20reuters", count = 75)
#query = twitter.search.tweets(q = "Fox%20News%20OR%20npr%20OR%20cnn%20reuters", count = 200, since ='2019-02-21', until= date )


#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print("Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"]))

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
x=1

for result in query["statuses"]:
    user = result["user"]["screen_name"]
    text = result["text"]
    created = result["created_at"]
    text = text.encode('ascii', 'replace')
    row.append([created, user, text])

  
   # csvwriter.writerow(row)
    x=x+1
    print("(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"]))

        #csvfile.close()


for i in range(len(row)) :
    for j in range(len(row[i])) :
        sheet.append_row(row[i])
# print()
#sheet.append_row(row, value_input_option='raw')

# Read CSV file contents


#1GafmIDcts7vFrZukvGy5dSnRCmPs-lvOtLoRl4z7AsQ
#sheet.import_csv(outfile)
print(sheet.id)
