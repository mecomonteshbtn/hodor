#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 07:10:33 2020

@author: meco
"""
import requests


url = 'http://158.69.76.135/level0.php'
playload = {'id': '1574', 'holdthedoor': 'submit'}

req = requests.get(url)
for i in range(1024):
    req = requests.post(url, data=playload)
print('Well done, Voting complete for level 0')
