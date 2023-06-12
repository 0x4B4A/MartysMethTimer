import tweepy
import time
import os
import requests

bearer = "AAAAAAAAAAAAAAAAAAAAALN8oAEAAAAAa9S0xtY1mpJ43NxTmTz1q5iN04U%3D3Mnhsp1FDaePg5WCKBxDWnJnGNUmjlvYFRdfOGfYMnaIcgLgQX"
api_token = "BfS2lC0v4ew1V7IZUlFZIZWmp"
api_secret = "ZGUebFMBzddZJVZwtvYJfqxGnOkqxaCdBYLHhQPpZd0poLm3tj"
access_token = "1668033824133922816-IfKJWy0y3VGmiB09V5XETxMyPBOPZz"
access_secret = "1fSXfOEsaX9naoHgrnQg65j2Q7NkQfgOKBhmLGBaTaYQp"

client = tweepy.Client(bearer, api_token, api_secret, access_token, access_secret)

auth = tweepy.OAuth1UserHandler(api_token, api_secret, access_token, access_secret)
api = tweepy.API(auth)

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
    mediaID=mediaID[105:124]
    print(mediaID)
    return(mediaID)

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

    mediaID=get_cat()
    client.create_tweet(text="testing :)", media_ids=[mediaID])
    print("tweet sent!")
    time.sleep(5)
    mediaID = get_cat()
    client.create_tweet(text="Marty can cook again!\nHe has cooked " + text + " times!", media_ids=[mediaID])
    print("marty can cook now")
    continue