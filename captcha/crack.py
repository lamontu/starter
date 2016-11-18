# -*- coding: utf-8 -*-

from PIL import Image
import hashlib
import time
import math
import os


im = Image.open("captcha.gif")
im.convert(mode='P')

his = im.histogram()
print(his)

values = {}
for i in range(256):
    values[i] = his[i]

for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(j, k)


# Obtain the black-white image of text 
im2 = Image.new('P', im.size, 255)

for x in range(im.size[1]):  # size = (width, height) = (len(y), len(x))
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        if pix == 220 or pix == 227:
            im2.putpixel((y,x), 0)

im2.show()


inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))
    inletter = False

print(letters)


# Obtain image of a single character
count = 0
for letter in letters:
    hasher = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    im3str = ("%s%s" % (time.time(), count)).encode('utf-8')
    hasher.update(im3str)
    im3.save("./%s.gif" % (hasher.hexdigest()))


class VectorCompare(object):
    # compute the norm of a vector
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    # compute the cosine of the angle between two vectors
    def relation(self, concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * 
                           self.magnitude(concordance2))


# convert a image to vector
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# load a training set
imageset = []
for letter in iconset:
    for img in os.listdir('./iconset/%s/' % (letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(
                buildvector(Image.open("./iconset/%s/%s" % (letter, img))))
        imageset.append({letter: temp})


# split verification code image to characters
count = 0
for letter in letters:
    hasher = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))

    guess = []

    for image in imageset:
        for x, y in image.items():
            if len(y) != 0:
                guess.append(
                    (v.relation(y[0], buildvector(im3)), x)
                )

    guess.sort(reverse=True)
    print("", guess[0])
    count += 1


