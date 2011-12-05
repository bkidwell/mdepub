import logging
import mdepub
from mdepub import options
from mdepub.filename import getFN
from mdepub.filename import clean
import os
from datetime import date
import sys
import shutil
from os.path import join, dirname, exists
from template import template_path
import re

log = logging.getLogger('create')

def run():
    log.debug("run()")

    print "Book title?"
    title = raw_input("> ")
    print "Author(s)?"
    author = raw_input("> ")
    print "Path to new book project files?\n[default: current directory]"
    path = raw_input("> ")

    today = re.sub("^0", "", date.today().strftime("%d %b %Y"))
    uuid = mdepub.new_id()
    filename = options.get("filename") or clean(title)

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
