"""Create empty project in this folder."""

from datetime import date
import logging
import os
from os.path import join, dirname, exists
import re
import sys
import shutil
import mdepub
from mdepub.filename import clean
from mdepub.filename import getFN
from mdepub.template import template_path

log = logging.getLogger('create')

def run():
    """Run this action."""

    log.debug("run()")

    print "Book title?"
    title = raw_input("> ")
    print "Author(s)?"
    author = raw_input("> ")
    print "Path to new book project files?\n[default: current directory]"
    path = raw_input("> ") or "."

    today = re.sub("^0", "", date.today().strftime("%d %b %Y"))
    uuid = mdepub.new_id()
    filename = mdepub.options.get("filename") or clean(title)

    log.debug("Creating project in \"%s\".", path)
    if not exists(path):
        os.makedirs(path)
    os.chdir(path)

    if exists("options.yaml"):
        log.fatal("An mdepub project file already exists in this path.")
        sys.exit(1)

    shutil.copyfile(join(template_path, "book.css"), "{}.css".format(filename))

    with open(join(template_path, "book.md"), 'r') as f: txt = f.read()
    with open("{}.md".format(filename), 'w') as f:
        f.write(
            txt.format(Title=title, Author=author)
        )

    with open(join(template_path, "options.yaml"), 'r') as f: txt = f.read()
    with open("options.yaml", 'w') as f:
        f.write(
            txt.format(Title=title, Author=author, Date=today, uuid=uuid)
        )
