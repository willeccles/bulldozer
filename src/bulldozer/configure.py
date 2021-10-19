import os
import sys
import importlib
import importlib.util

from bulldozer import make

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

    # TODO nicer logging
    if not 'name' in vars(project):
        print("Error: configuration does not contain 'name'")
        exit(1)

    print(project.name)
    if 'version' in vars(project):
        print(project.version)

    if not os.access(os.path.join(args.path, 'build'), os.F_OK):
        os.mkdir(os.path.join(args.path, 'build'))

    make.Generate(args, project)
