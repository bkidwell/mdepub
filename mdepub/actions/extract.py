import logging
from os.path import join, exists, abspath, dirname
import os
import mdepub
from mdepub import arguments
from mdepub import project_path
from mdepub.filename import getFN
from mdepub.filename import clean
import sys
from zipfile import ZipFile
from StringIO import StringIO
import yaml

log = logging.getLogger('extract')

def run():
    log.debug("run()")

    old_cwd = os.getcwd()

    if arguments.fromf is None:
        log.fatal("No input file specified.")
        sys.exit(0)

    fromf = abspath(arguments.fromf)

    with ZipFile(fromf, 'r') as epub:
        with epub.open("META-INF/source.mdepub.zip", 'r') as src_item:
            src_stream = StringIO(src_item.read())

    with ZipFile(src_stream, 'r') as src_zip:
        with src_zip.open("options.yaml", 'r') as src_opt_item:
            src_opt = yaml.load(src_opt_item)

        #print yaml.dump(src_opt)

        if arguments.to is None:
            arguments.to = join(old_cwd, clean(src_opt.get('title')))
        if arguments.to is None:
            log.fatal("Can't determine output path name")
            sys.exit(1)

        if not exists(arguments.to):
            os.makedirs(arguments.to)
        os.chdir(arguments.to)

        src_zip.extractall()

    src_stream.close()
    os.chdir(old_cwd)
