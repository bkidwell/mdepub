import logging
import os.path
import mdepub
from mdepub import project_path
from mdepub.filename import getFN

log = logging.getLogger('clean')

def run():
    log.debug("run()")
    mdepub.require_opts_file()
    os.chdir(project_path)

    for ext in ['epub', 'html', 'zip']:
        f = getFN(ext)
        if os.path.exists(f):
            os.remove(f)
