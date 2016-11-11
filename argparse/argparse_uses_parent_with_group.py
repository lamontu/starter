# -*- coding: utf-8 -*-

import argparse


parser_parent = argparse.ArgumentParser(add_help=False)

group = parser_parent.add_argument_group('authentication')

group.add_argument('--user', action="store")
group.add_argument('--password', action="store")


parser = argparse.ArgumentParser(parents=[parser_parent])

parser.add_argument('--local-arg', action="store_true", default=False)

print(parser.parse_args())


