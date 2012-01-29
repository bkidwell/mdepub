"""Extract the source files from the given Epub file."""

import logging
import os
from os.path import join, exists, abspath, dirname
from StringIO import StringIO
import sys
import yaml
from zipfile import ZipFile

import mdepub
from mdepub.filename import clean
from mdepub.filename import getFN

log = logging.getLogger('extract')

def run():
    """Run this action."""

    log.debug("run()")

    old_cwd = os.getcwd()

    arguments = mdepub.arguments
    project_path = mdepub.project_path

    if arguments.fromfile is None:
        log.fatal("No input file specified.")
        sys.exit(0)

    fromf = abspath(arguments.fromfile)

    with ZipFile(fromf, 'r') as epub:
        with epub.open("META-INF/source/mdepub_source.zip", 'r') as src_item:
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
