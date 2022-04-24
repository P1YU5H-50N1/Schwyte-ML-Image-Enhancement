import os
import time

from .API import fetch_data, post_imgs
from .ISR  import super_resolve

while(True):
    time.sleep(60)
    hi_res = {}
    data = fetch_data() # stores img in tmp_img/low_res, returns a dict of usernames and list of image paths
    for key in data:
        status, paths = super_resolve(data[key]) # stores image in tmp_img/hi_res and returns status if it is done correctly and list of image paths
        if status == True:
            hi_res[key] = paths
    
    for key in hi_res:
        post_imgs(hi_res[key],key) # passes on the username with list of image paths to be posted
                
        
    
    


