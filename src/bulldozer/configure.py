import os
import sys
import importlib
import importlib.util

# TODO move this to a more accessible location for other source files
def LoadProject(project_root: str):
    spec = importlib.util.spec_from_file_location('',
            os.path.join(project_root, 'dozer.py'))
    # TODO where to put this so that __pycache__ isn't everywhere
    spec.cached = None
    project = importlib.util.module_from_spec(spec)
    #sys.modules['project'] = project
    spec.loader.exec_module(project)
    return project

def Configure(args):
    project = LoadProject(args.path)
    print(project.CoolFunction())
