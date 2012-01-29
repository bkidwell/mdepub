"""Assign a new ID for this project in options.yaml."""

import logging
import os
import re
import mdepub
from mdepub import new_id

log = logging.getLogger('newid')

r_uuid = re.compile(
    r'^([ \t]*)uuid:([ \t]*)([\S]*)([ \t]*)$',
    re.MULTILINE
)

def run():
    """Run this action."""

    options = mdepub.options
    project_path = mdepub.project_path

    log.debug("run()")
    mdepub.require_opts_file()
    os.chdir(project_path)

    if 'uuid' in options:
        # replace existing uuid
        with open("options.yaml", "r") as f: txt = f.read()
        txt = r_uuid.sub(
            r'\g<1>uuid:\g<2>' + str(new_id()) + r'\g<4>',
            txt
        )
        #print txt
        with open("options.yaml", "w") as f: f.write(txt)
    else:
        # add new uuid field to end of file
        with open("options.yaml", "a") as f:
            f.write("\nuuid: {0}\n".format(new_id()))
