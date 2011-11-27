import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path
from zipfile import ZipFile
from mdepub.filename import getFN

log = logging.getLogger('archive')

def run():
    log.debug("run()")

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
