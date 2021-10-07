import os
import sys
import importlib

def Configure(args):
    sys.path.append(args.path)
    project = importlib.import_module('dozer')
    print(project.CoolFunction())
