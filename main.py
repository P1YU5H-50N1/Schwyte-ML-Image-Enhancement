import os
import time
from ISR.models import RDN
from API import fetch_data, post_result
from ISR_resolve  import super_resolve
import tweepy

BEARER_TOKEN=os.environ.get('BEARER_TOKEN') or ""
API_KEY=os.environ.get('API_KEY') or ""
API_KEY_SECRET=os.environ.get('API_KEY_SECRET') or ""
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN') or ""
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET') or "" 
try:
    rdn = RDN(weights='noise-cancel')
    client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, 
                                consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, 
                                access_token_secret=ACCESS_TOKEN_SECRET)
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
except Exception as e:
    print(f"Error occured: {e}")
    quit()


while(True):
    data = fetch_data(client) 
    image_paths = [tweet['low_res_imgs'] for tweet in data]
    im_paths = []
    for path_list in image_paths:
        for path in path_list:
            im_paths.append(path)
    image_paths = super_resolve(im_paths,rdn)
    
    for tweet in data:
        post_result(tweet,client,api)
    
    time.sleep(60)
    
    # hi_res = {}
    
    # for key in data:
    #     status, paths = super_resolve(data[key]) # stores image in tmp_img/hi_res and returns status if it is done correctly and list of image paths
    #     if status == True:
    #         hi_res[key] = paths
    
    # for key in hi_res:
    #     post_imgs(hi_res[key],key) # passes on the username with list of image paths to be posted
                
        
    
    


