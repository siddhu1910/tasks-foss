# code to update your twitter status from command line interface
import tweepy
consumer_key='XKiwkkilYyD8p6B8sxZvmNuW4'
consumer_secret='ePOyEbRnmZxQIDa7d0le2QSSNScIh6GBLhvKrPiWAnB200HQyz'
access_token='1052785060598796288-5JsYYLvlTRYCk4hS8jTpVBQPjLtzZx'
access_token_secret='jC0cI9UAsGrHyn9lsSa0yHdh0XTfgWGV7DQkKpYyTE7y7'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
api.update_status(input("status to be updated: "))
print("status successfully updated in twitter!!")
