import urllib.request
from PIL import Image
import time
import ctypes

url = "https://cdn.star.nesdis.noaa.gov/GOES17/ABI/FD/GEOCOLOR/5424x5424.jpg"
SPI_SETDESKWALLPAPER = 20 
latest_original_path= r'C:\Users\sfeng\Projects\RefreshWallpaper\latest.jpg'
cropped_path= r'C:\Users\sfeng\Projects\RefreshWallpaper\cropped.jpg'

while(True):
    try:
        urllib.request.urlretrieve(url, latest_original_path)
        img = Image.open(latest_original_path) 
        w, h = img.size
        cropped = img.crop((0, 0, w, h * 0.4))
        cropped.save(cropped_path)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, cropped_path , 0)
    except Exception as e:
        print(e)
    time.sleep(600)