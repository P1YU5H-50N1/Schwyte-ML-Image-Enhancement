#! /bin/bash
DIRECTORY='tmp'
if [ ! -d "$DIRECTORY" ]; then
    mkdir tmp && mkdir tmp/hi_res && mkdir tmp/low_res
  # Control will enter here if $DIRECTORY doesn't exist.
fi
pip install 'h5py==2.10.0' --force-reinstall
pip install git+https://github.com/idealo/image-super-resolution