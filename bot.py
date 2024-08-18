git clone https://github.com/tweepy/tweepy.gitcd tweepypython setup.py install
import tweepyimport Tkinter

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)auth.set_access_token(access_token, access_token_secret)api = tweepy.API(auth)
user = api.me()print (user.name)
