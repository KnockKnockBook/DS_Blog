#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:37:17 2021

@author: jonahbrown-joel
"""

import sys


from flask_frozen import Freezer
sys.path.append('/Users/jonahbrown-joel/Library/Mobile Documents/com~apple~CloudDocs/Data_Science_Blog/Blog_App')
from flask_app import app
    
#app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()    