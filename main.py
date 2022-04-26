import os
import time

from API import fetch_data, post_result
from ISR  import super_resolve

while(True):
    data = fetch_data() 
    image_paths = [tweet['low_res_img'] for tweet in data]
    image_paths = super_resolve(image_paths)
    
    for tweet in data:
        post_result(tweet)
    
    time.sleep(60)
    
    # hi_res = {}
    
    # for key in data:
    #     status, paths = super_resolve(data[key]) # stores image in tmp_img/hi_res and returns status if it is done correctly and list of image paths
    #     if status == True:
    #         hi_res[key] = paths
    
    # for key in hi_res:
    #     post_imgs(hi_res[key],key) # passes on the username with list of image paths to be posted
                
        
    
    


