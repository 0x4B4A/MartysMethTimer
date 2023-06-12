import tweepy
import time
import os

bearer = ""
api_token = ""
api_secret = ""
access_token = ""
access_secret = ""

client = tweepy.Client(bearer, api_token, api_secret, access_token, access_secret)

auth = tweepy.OAuth1UserHandler(api_token, api_secret, access_token, access_secret)
api = tweepy.API(auth)

mediaID = "1668082606523424768"
print(mediaID)

while True:
    print("press ENTER to tweet!")
    input(" ")

    num = open('times.txt', 'r+')
    text = num.read()
    text_num = int(text)
    print(text)
    num.close()
    os.remove("times.txt")
    num = open('times.txt', 'x')
    num.close()
    num = open('times.txt', 'r+')
    num.write(str(text_num+1))
    num.close()


    client.create_tweet(text="Marty has started cooking! He has cooked " + text + " times!\nTweeting in another two hours...", media_ids=[mediaID])
    print("tweet sent!")
    time.sleep(7200)
    client.create_tweet(text="Marty can cook again!\nHe has cooked " + text + " times!", media_ids=[mediaID])
    print("marty can cook now")
    continue