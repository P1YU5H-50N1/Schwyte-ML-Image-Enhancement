
import numpy as np
from PIL import Image
from ISR.models import RDN

rdn = RDN(weights='noise-cancel')

def super_resolve(img_paths):
    '''converts low res to hi res images
    args: image paths in tmp_img
    returns: status if converted correctly and list of paths of super resolved images'''
    low_res_dir = "tmp/low_res/"
    hi_res_dir = "tmp/hi_res/"
    for path in img_paths:
        file = low_res_dir + path
        save_path = hi_res_dir + path
        img = Image.open(file)
        lr_img = np.array(img)
        sr_img = rdn.predict(lr_img)
        img = Image.fromarray(sr_img)
        Image.save(save_path)
    
    return img_paths
        
        