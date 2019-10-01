# code to update your twitter status from command line interface
import tweepy
consumer_key='<your consumer key>'
consumer_secret='<your consumer private>'
access_token='<your access token>'
access_token_secret='<your acess token private>'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
api.update_status(input("status to be updated: "))
print("status successfully updated in twitter!!")
