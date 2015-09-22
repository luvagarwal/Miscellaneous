#!/usr/bin/env python
from datetime import datetime, timedelta
import os

INTELLIGENCE_FACTOR = 2
FILE_BASE_DIR = '/home/luv/notes/Notes/DailyWork/'

MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
         'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

TODAY = datetime.today()
if TODAY.hour < 7:
    TODAY -= timedelta(1)

for i in xrange(1, 10):
    date = TODAY-timedelta(INTELLIGENCE_FACTOR**i)
    if date.year == 2015:
        fdir = FILE_BASE_DIR + str(date.day) + MONTH[date.month-1] + "/"
        os.system('gedit ' + fdir + "index")
        os.system('gedit ' + fdir + "words")
        if date.month > 5:
            os.system('gedit ' + fdir + "work-today")

