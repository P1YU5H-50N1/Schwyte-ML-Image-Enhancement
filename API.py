import tweepy
from tweepy.errors import Unauthorized
import os
import wget

BEARER_TOKEN=os.environ.get('BEARER_TOKEN') or ""
API_KEY=os.environ.get('API_KEY') or ""
API_KEY_SECRET=os.environ.get('API_KEY_SECRET') or ""
ACCESS_TOKEN=os.environ.get('ACCESS_TOKEN') or ""
ACCESS_TOKEN_SECRET=os.environ.get('ACCESS_TOKEN_SECRET') or "" 

def fetch_data():
    ''' Returns an array of dicts with tweets, username, author_id, tweet_id, media_keys, low_res_image_path saved in a folder tmp_img/low_res
    [{'tweet': '', 'username': '', 'author_id': int, 'tweet_id': number, 'media_keys': [''], 'low_res_img': ['']}]
    '''
    tweets = []
    
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, 
                            consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, 
                            access_token_secret=ACCESS_TOKEN_SECRET)
        schwyte = client.get_me()
        user_id = schwyte.data.id
        public_tweets = client.get_users_mentions(user_id,expansions='attachments.media_keys',media_fields=["url","preview_image_url"])

        for response in tweepy.Paginator(client.get_users_mentions,user_id,expansions=['attachments.media_keys','author_id'],media_fields=["url","height","width","preview_image_url"]):
            print(response)
            try:
                media = {m["media_key"]: m for m in response.includes['media']}
            except:
                media = {"key":None}

            client_user_ids = [tweet.author_id for tweet in response.data]
            # # print(client_user_ids)

            client_users = client.get_users(ids = client_user_ids)
            client_user_names = {user.id:user.username for user in client_users.data}
            # # print(client_user_names)
            
            for tweet in response.data:
                # print('tweet:',tweet.text,"\n author_id:",tweet.author_id,"\n tweet_id: ",tweet.id,"\n")
                current_tweet = {
                    "tweet":tweet.text,
                    "username": client_user_names[tweet.author_id],
                    "author_id":tweet.author_id,
                    "tweet_id":tweet.id
                }
                if tweet.attachments:
                    attachments = tweet['attachments']
                    media_keys = attachments['media_keys']
                    current_tweet['media_keys'] = media_keys
                    current_tweet["low_res_imgs"] = []
                    
                    for key in media_keys: 
                        if media[key].type == "photo":
                            file_name = media[key].url.replace("https://pbs.twimg.com/media/","")
                            file_loc = "tmp/low_res/" + file_name
                            current_tweet["low_res_img"].append(file_name)
                            if not os.path.exists(file_loc):
                                wget.download(media[key].url,file_loc)
                            tweets.append(current_tweet)


        
    except Unauthorized:
        print("Unauthorized! Check API keys")
        quit()
    except Exception as e:
        print(f"Error occured: {e}")
        quit()
    return tweets

def post_imgs(img_paths, username):
    '''Posts a list of images with a msg mentioning twitter username'''
    
def create_new():
    try:
        client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, 
                            consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, 
                            access_token_secret=ACCESS_TOKEN_SECRET)
        res = client.create_tweet(text=" #2 I'll be up in some time! @ViewsOfPiyush",media_ids=[upload_media()])
        print(res) 
        '''Response(data={'id': '1518491368535982083', 'text': "I'll be up in some time! @ViewsOfPiyush"}, includes={}, errors=[], meta={})'''
        
    except Unauthorized:
        print("Unauthorized! Check API keys")
        quit()
    except Exception as e:
        print(f"Error occured: {e}")
        quit()
        
def upload_media(img=""):
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    m1 = media = api.media_upload('tmp/low_res/FL91SNMacAIde-7.jpg')
    print(m1,m1.media_id)
    return m1.media_id
    '''
    Media(_api=<tweepy.api.API object at 0x7f3b0d18b250>, media_id=1518492842087239680, media_id_string='1518492842087239680', size=89095, expires_after_secs=86400, image={'image_type': 'image/jpeg', 'w': 1200, 'h': 625}) 
    1518492842087239680
    '''
# create_new()
# upload_media()