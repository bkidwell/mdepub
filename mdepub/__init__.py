import logging
import os
import yaml
from mdepub.argumentparser import ArgumentParser
options = None
import filename
import uuid

VERSION = "0.1"

def new_id():
    return uuid.uuid4()

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('mdepub')

project_path = os.getcwd()
log.debug("Working path: %s", project_path)

options_file = os.path.join(project_path, "options.yaml")
if os.path.exists(options_file):
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
    log.debug("options.yaml not found")

arguments = ArgumentParser().parse_args()
