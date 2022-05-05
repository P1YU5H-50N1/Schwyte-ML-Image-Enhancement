#! /bin/bash
DIRECTORY='tmp'
if [ ! -d "$DIRECTORY" ]; then
    mkdir tmp && mkdir tmp/hi_res && mkdir tmp/low_res
fi
pip install 'h5py==2.10.0' --force-reinstall
# pip install git+https://github.com/idealo/image-super-resolution
pip install ISR
pip install -r requirements.txt