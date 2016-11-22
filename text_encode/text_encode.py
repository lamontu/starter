# -*- coding: utf-8 -*-

import sys
import os
import argparse
from chardet.universaldetector import UniversalDetector


parser = argparse.ArgumentParser(description="Detect and convert text encode")

parser.add_argument('filePaths', nargs='+',
                    help='path of the file to detect or convert')
parser.add_argument('-e', '--encoding', nargs='?', const='utf-8',
                     help='''
Supported Encode (not sure):
    ASCII, Big5, GB2312/GB18030, HZ-GB-2312, SHIFT-JIS, KOI8-R, MacCyrillic,
    TIS-620,
    UTF-8, UTF-16, UTF-32,
    EUC-TW, EUC-JP, EUC-KR,
    ISO-2022-CN, ISO-2022-JP, ISO-2022-KR, ISO-8859-1, ISO-8859-2, ISO-8859-5,
    ISO-8859-7, ISO-8859-8,
    IBM855, IBM866,
    windows-1250, windows-1251, windows-1252, windows-1253, windows-1255
''')
parser.add_argument('-o', '--output', help='output directory')


args = parser.parse_args()
print(args.output, type(args.output))

if args.output != None:
    if not args.encoding:
        args.encoding = 'utf-8'
    if not os.path.isdir(args.output):
        print('Invalid Directory: ' + args.output)
        sys.exit()
    else:
        if args.output[-1] != '/':
            args.output += '/'

detector = UniversalDetector()

print()

print('Encoding (Confidence)', ':', 'File path')
for filePath in args.filePaths:
    if not os.path.isfile(filePath):
        print('Invalid Path: ' + filePath)
        continue
    detector.reset()
    for each in open(filePath, 'rb'):
        detector.feed(each)
        if detector.done:
            break
    detector.close()
    charEncoding = detector.result['encoding']
    confidence = detector.result['confidence']
    if charEncoding is None:
        charEncoding = 'Unknown'
        confidence = 0.99
    print('{} {:>12} : {}'.format(charEncoding.rjust(8),
                           '(' + str(confidence * 100) + '%)', filePath))
    if args.encoding and charEncoding != 'Unknown' and confidence > 0.6:
        outputPath = args.output + os.path.basename(
                         filePath) if args.output else filePath 
        with open(filePath, 'r', encoding=charEncoding, errors='replace') as f:
            temp = f.read()
        with open(outputPath, 'w', encoding=args.encoding,
                  errors='replace') as f:
            f.write(temp)


