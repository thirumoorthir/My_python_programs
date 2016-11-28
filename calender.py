 #!/usr/bin/python:
# -*- coding: utf-8 -*-
from sys import argv
import tweepy
import facebook
script, first = argv 

def get_api_tweet(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
def main_tweet():
  cfg = { 
    "consumer_key"        : " ",
    "consumer_secret"     : " ",
    "access_token"        : " - ",
    "access_token_secret" : " " 
    }
  api = get_api_tweet(cfg)
  tweet = "இன்ரைய நாள் காட்டி  #tamilcalender (©belongs to watermarked party),"
 #tweet = 'test'
  image_path = "%s"%first
  status = api.update_with_media(image_path,tweet)
if __name__ == "__main__":
 main_tweet()

def main():
  cfg = {
    "page_id"      : " ",
    "access_token" : " &"   
    }
  api = get_api(cfg)
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  #caption = ''
  caption = "இன்ரைய நாள் காட்டி  #tamilcalender (©belongs to watermarked party)" 
  albumid = ''   
  with open(first,"rb") as image:
          posted_image_id = graph.put_photo(image, caption, albumid)
  return graph
if __name__ == "__main__":
  main()

