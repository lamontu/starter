# -*- coding: utf-8 -*-

import os
import markdown
from bs4 import BeautifulSoup
import sys


class MarkdownToHtml(object):
    headTag = '<head><meta charset="utf-8"></head>'

    def __init__(self, cssFilePass=None):
        if cssFilePass != None:
            self.genStyle(cssFilePath)

    def genStyle(self, cssFilePath):
        with open(cssFilePath, 'r') as f:
            cssString = f.read()
        self.headTag = self.headTag[:-7] + '<style type="text/css">{}</style>'.format(cssString) + self.headTag[-7:]

    def markdownToHtml(self, sourceFilePath, destinationDirectory=None,
                       outputFileName=None):
        if not destinationDirectory:
            destinationDirectory = os.path.dirname(os.path.abspath(source))
        if not outputFileName:
            outputFileName = os.path.splitext(
                os.path.basename(sourceFilePath))[0] + '.html'
        if destinationDirectory[-1] != '/':
            destinationDirectory += '/'
        with open(sourceFilePath, 'r', encoding='utf-8') as f:
            markdownText = f.read()
        rawHtml = self.headTag + markdown.markdown(markdownText,
                                                   output_format='html5')
        beautifyHtml = BeautifulSoup(rawHtml, 'html5lib').prettify()
        with open(destinationDirectory + outputFileName, 'w',
                  encoding='utf-8') as f:
            f.write(beautifyHtml)


if __name__ == '__main__':
    mth = MarkdownToHtml()
    argv = sys.argv[1:]
    outputDirectory = None
    if '-s' in argv:
        cssArgIndex = argv.index('-s') + 1
        cssFilePath = argv[cssArgIndex]
        if not os.path.isfile(cssFilePath):
            print('Invalid Path: ' + cssFilePath)
            sys.exit()
        mth.genStyle(cssFilePath)
        argv.pop(cssArgIndex)
        argv.pop(cssArgIndex - 1)
    if '-o' in argv:
        dirArgIndex = argv.index('-o') + 1
        outputDirectory = argv[dirArgIndex]
        if not os.path.isdir(outputDirectory):
            print('Invalid Directory: ' + outputDirectory)
            sys.exit()
        argv.pop(dirArgIndex)
        argv.pop(dirArgIndex - 1)

    for filePath in argv:
        if os.path.isfile(filePath):
            mth.markdownToHtml(filePath, outputDirectory)
        else:
            print('Invalid Path: ' + filePath)


"""
usage:
    python markdown_html.py test.md [test1.md test2.md] -s ./GithubMarkdownCSS.css -o ./OutputDirectory
""" 


