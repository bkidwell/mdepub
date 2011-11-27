import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path

log = logging.getLogger('html')

def run():
    log.debug("run()")

    os.chdir(project_path)

    css_file = "%s.css" % options['filename']

    args = ["pandoc", "--standalone", "--email-obfuscation=none"]

    if os.path.exists(os.path.join(project_path, css_file)):
        args.extend(["-c", css_file])
    if options['smart quotes']:
        args.append("--smart")
    args.append("%s.md" % options['filename'])

    shell.save_output(args, "%s.html" % options['filename'])

# TODO: check for broken internal links
