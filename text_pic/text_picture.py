# -*- coding: utf-8 -*-
"""
This program can NOT convert traditional chinese to picture,
no matter using what font.
"""
from PIL import Image, ImageDraw, ImageFont 
import os


def pasteWord(words, fontpath):
    os.chdir('./word')
    words = words.strip()
    text_list = words.split(' ')
    length = len(text_list)
    for i in range(length):
        text = text_list[i]
        imgName = text_list[i] + '.png'
        if os.path.isfile(imgName):
            continue
        else:
            paste(text, fontpath, imgName)


def paste(text, fontpath, imgName):
    im = Image.new('RGB', (30, 30), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(fontpath, 22)

    dr.text((3, 0), text, font=font, fill='#000000')

    im.save(imgName) 


if __name__ == '__main__':
    f = open('word.txt', 'r')
    words = f.readlines()[0]
    f.close()

    fontpath = "/Library/Fonts/hanyi.ttf"
    pasteWord(words, fontpath)


