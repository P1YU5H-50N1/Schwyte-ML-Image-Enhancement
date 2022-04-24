import tweepy
from tweepy.errors import Unauthorized
import os

BEARER_TOKEN=os.environ.get('BEARER_TOKEN') or ""
API_KEY=os.environ.get('API_KEY') or ""
API_KEY_SECRET=os.environ.get('API_KEY_SECRET') or ""
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN') or ""
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET') or "" 

def fetch_data():
    ''' Returns a dictionary with keys as usernames and values as list of image_path saved in a folder tmp_img/low_res'''
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, 
                            consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, 
                            access_token_secret=ACCESS_TOKEN_SECRET)
        schwyte = client.get_me()
        user_id = schwyte.data.id
        
    except Unauthorized:
        print("Unauthorized! Check API keys")
        quit()
    except Exception as e:
        print(f"Error occured: {e}")
        quit()
        
    return {}

def post_imgs(img_paths, username):
    '''Posts a list of images with a msg mentioning twitter username'''
    
fetch_data()