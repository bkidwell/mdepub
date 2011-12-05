import logging
import os
import yaml
from mdepub.argumentparser import ArgumentParser
options = None
import filename
import uuid
import sys

VERSION = "0.1"

def new_id():
    return uuid.uuid4()

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('mdepub')

project_path = os.getcwd()
log.debug("Working path: %s", project_path)

options_file = os.path.join(project_path, "options.yaml")
options_loaded = False
if os.path.exists(options_file):
    options_loaded = True
    log.debug("Loading options.yaml")
    options = yaml.load(open("options.yaml"))
    if VERSION.split(".") < (options.get("require mdepub version") or "").split("."):
        log.fatal("This project requires at least version %s of mdepub.", options["require mdepub version"])
        sys.exit(1)
    #print yaml.dump(options)
    #print options.keys()
    if not options.get('filename'):
        options['filename'] = filename.clean(options['title'])
    log.debug("Filename: %s", options['filename'])
else:
    options = yaml.load("dummy: 0")
    log.debug("options.yaml not found")

arguments = ArgumentParser().parse_args()

if arguments.filename:
    options['filename'] = arguments.filename

def require_opts_file():
    if options_loaded: return
    log.fatal("No options.yaml file found for this project.")
    sys.exit(1)
