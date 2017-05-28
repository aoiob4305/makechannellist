# -*- coding:utf-8 -*-

import csv

with open('skChannels.csv', newline='',encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    print('#EXTM3U')
    for row in spamreader:
        if row[3] != '':
            print('#EXTINF:-1 tvg-id="%s" tvg-chnum="%s",%s\nudp://%s:%s' % (row[0],row[2],row[1],row[3],row[4]))

