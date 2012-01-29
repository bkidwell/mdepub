"""Delete output files except Epub package."""

import logging
import os.path
import mdepub
from mdepub.filename import getFN

log = logging.getLogger('clean')

def run():
    """Run this action."""

    log.debug("run()")
    mdepub.require_opts_file()
    os.chdir(mdepub.project_path)

    for ext in ['epub', 'html', 'zip']:
        f = getFN(ext)
        if os.path.exists(f):
            os.remove(f)
