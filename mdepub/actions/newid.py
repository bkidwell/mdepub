import logging
import mdepub
from mdepub import new_id
from mdepub import project_path
from mdepub import options
import re
import os

# TODO: implement 'clean' action

log = logging.getLogger('newid')

r_uuid = re.compile(
    r'^([ \t]*)uuid:([ \t]*)([\S]*)([ \t]*)$',
    re.MULTILINE
)

def run():
    log.debug("run()")
    os.chdir(project_path)

    print mdepub.options
    if 'uuid' in options:
        # replace existing uuid
        with open("options.yaml", "r") as f: txt = f.read()
        txt = r_uuid.sub(
            r'\g<1>uuid:\g<2>' + str(new_id()) + r'\g<4>',
            txt
        )
        print txt
        with open("options.yaml", "w") as f: f.write(txt)
    else:
        # add new uuid field to end of file
        with open("options.yaml", "a") as f:
            f.write("\nuuid: {0}\n".format(new_id()))
