import urllib.request
from PIL import Image
from wallpaper import set_wallpaper, get_wallpaper
import time
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Start...')

url = "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/5424x5424.jpg"

while(True):
    try:
        urllib.request.urlretrieve(url, 'latest.jpg')
        img = Image.open("latest.jpg") 
        w, h = img.size
        cropped = img.crop((0, 0, w, h * 0.4))
        cropped.save("cropped.jpg")
        set_wallpaper("cropped.jpg")
        logging.info('Updated wall paper')
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
    time.sleep(600)