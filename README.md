# COLISION WARNING IN ADAS


## Install package:
pip install -r requirements.txt

## Run this project:
python object_tracker.py --video ./data/video/test4.mp4 --output ./outputs/test4.avi


## if you want to change focal length for estimating distance, you can edit file FocalLength.py and run: 
python FocalLength.py --image car-focalLength.png --knownDistanceMet 10 --heightObject 1.6