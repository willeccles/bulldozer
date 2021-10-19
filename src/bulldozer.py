#!/usr/bin/env python3

import os
import sys
import importlib
import argparse

from bulldozer.configure import Configure
#from bulldozer.build import Build

parser = argparse.ArgumentParser(description='Bulldozer')
subparsers = parser.add_subparsers(title="operations",
        description="bulldozer build system operations", required=True,
        metavar="OP", dest='op')

base_args = argparse.ArgumentParser(add_help=False)
base_args.add_argument('-v', '--verbose', action='store_true',
        help='enable verbose operation')

p_configure = subparsers.add_parser('configure', aliases=['setup', 'config'],
        parents=[base_args], help='configure a project')
p_configure.add_argument('path', metavar='PATH', type=str, nargs='?',
        help='path to the project root directory', default=os.getcwd())
p_configure.set_defaults(func=Configure)

p_build = subparsers.add_parser('build', parents=[base_args],
        help='build a project')
p_build.add_argument('path', metavar='PATH', type=str, nargs='?',
        help='path to the project build directory', default='./build')
#p_build.set_defaults(func=Build)

args = parser.parse_args()
args.path = os.path.abspath(args.path)
args.func(args)


#sys.path.append(os.getcwd())
#dozer = importlib.import_module('dozer')

#print(dozer.CoolFunction())
