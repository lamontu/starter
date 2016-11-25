

"""
This program docopt_demo shows the usage of module docopt.

Usage: docopt_demo [options] [FILE]

Options:
  -h --help             Show this on screen.
  -v --version          Show version.
  -c --colors           Show colored output.
  -b --bold             Output bold characters.
  --bg=(BLACK|WHITE)    Specify the background color.
  --contrast=<factor>   Manually set contrast [default: 1.5].
  --alt-chars           Use an alternate set of characters.
"""
# Above text must be put in the top of this file

# -*- coding: utf-8 -*-

from docopt import docopt


__version__ = 'docopt_demo 1.0'


def main():
    arguments = docopt(__doc__, version=__version__)

    if arguments['FILE']:
        print("process using arguments >>>>")
        print( arguments)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()


