import tweepy
import time
import os
import requests

bearer = ""
api_token = ""
api_secret = ""
access_token = ""
access_secret = ""

client = tweepy.Client(bearer, api_token, api_secret, access_token, access_secret)

auth = tweepy.OAuth1UserHandler(api_token, api_secret, access_token, access_secret)
api = tweepy.API(auth)
#asdfas
mediaID = "1668082606523424768"

def get_cat():
    test=requests.get("https://api.thecatapi.com/v1/images/search")
    test2 = test.json()
    test3 = test2[0]["url"]
    test1_0=requests.get(test3)
    with open('cat.png', 'wb') as f:
        f.write(test1_0.content)

    mediaID=api.media_upload(filename='cat.png')
    print(mediaID)
    mediaID=str(mediaID)
    mediaID_num=mediaID.find('media_id_string=')
    mediaID=mediaID[mediaID_num+17:mediaID_num+36]
    print(mediaID)
    return(mediaID)

def create_tweet(text):
    mediaID = get_cat()
    client.create_tweet(text=text, media_ids=[mediaID])
    print("tweet sent!")

while True:
    print("type 'meth' to tweet meth cooking!\ntype 'logoff' to tweet logoff tweet")
    plyr_input = input("> ")

    if plyr_input == "meth":

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

        create_tweet("Marty has started cooking! He has cooked " + text + " times!\nTweeting in another two hours...")
        for i in range(0,7200):
            print(str(7200-i))
            time.sleep(1)
        create_tweet("Marty can cook again!\nHe has cooked " + text + " times!")
        continue

    elif plyr_input == "logoff":
        create_tweet("Marty has logged off of NoPixel.\nHave a good night everyone!")