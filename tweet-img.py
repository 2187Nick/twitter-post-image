import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Client for Twitter v2
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret)

# Authenticate to Twitter v1
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create v1 API object
api = tweepy.API(auth)

api.verify_credentials()
print("Authentication OK")

media = api.media_upload("/imagefolder/test_image.png")
print("media: ", media.media_id)

tweet = "test tweet"
client.create_tweet(text=tweet, media_ids=[media.media_id])
