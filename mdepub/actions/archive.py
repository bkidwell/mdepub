"""Archive source files to zip file."""

import logging
import os
from zipfile import ZipFile
import mdepub
from mdepub import shell
from mdepub.filename import getFN

log = logging.getLogger('archive')

def run():
    """Run this action."""

    options = mdepub.options
    project_path = mdepub.project_path

    log.debug("run()")
    mdepub.require_opts_file()

    os.chdir(project_path)

    skip = [
        "./" + getFN("html"),
        "./" + getFN("epub"),
        "./" + getFN("zip")
    ]

    with ZipFile(getFN("zip"), 'w') as zip:
        for root, dirs, files in os.walk("."):
            for file in files:
                fpath = os.path.join(root, file)
                if fpath not in skip:
                    zip.write(fpath)
