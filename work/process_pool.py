# -*- coding: utf-8 -*-

import multiprocessing
import time
import sys
import os


filehandler = open('download.txt','r')
filehandler.seek(0)
textlist = filehandler.readlines()

manger = multiprocessing.Manger()
l = manger.list()
for line in textlist:
    line = line.strip('\n')
    l.append(line)
lineCount = len(l)


def downloadPage(x):
    print('download %s ------ %s' % (x, l[x]))
    os.system('wget %s' % l[x])

pool = multiprocessing.Pool(3)
for i in range(lineCount):
    res = pool.apply_async(downloadPage, (i,))

pool.close()
pool.join()

if res.successful():
    print('successful')

