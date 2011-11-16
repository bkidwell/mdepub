import logging
import os
import yaml
from mdepub.argumentparser import ArgumentParser
import filename

# actions:
import clean

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('mdepub')

project_path = os.getcwd()
log.debug("Working path: %s", project_path)

options_file = os.path.join(project_path, "options.yaml")
options = None
if os.path.exists(options_file):
    log.debug("Loading options.yaml")
    options = yaml.load(open("options.yaml"))
    #print yaml.dump(options)
    #print options.keys()
    if not 'filename' in options:
        options['filename'] = filename.clean(options['title'])
    log.debug("Filename: %s", options['filename'])
else:
    log.debug("options.yaml not found")

arguments = ArgumentParser().parse_args()
