import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path

log = logging.getLogger('epub')


def quote(text):
    return text.replace('"', '\'')

def run():
    log.debug("run()")

    os.chdir(project_path)

    args = [
        "ebook-convert",
        "\"%s.html\"" % options['filename'],
        "\"%s.epub\"" % options['filename'],
        "--authors=\"%s\"" % quote(options['authors']),
        "--author-sort=\"%s\"" % quote(options['author sort']),
        "--pubdate=\"%s\"" % options['publication date'],
        "--title=\"%s\"" % quote(options['title']),
        "--tags=\"%s\"" % quote(','.join(options['tags']))
    ]
    args.append("--chapter=\"//h:h%s\"" % options['chapter head level'])
    tmp = []
    for i in range(options['chapter head level']):
        if len(tmp) > 0: tmp.append("or")
        tmp.append("name()='h%s'" % str(i + 1))
    args.append(
        "--level1-toc=\"//*[%s]\"" % " ".join(tmp)
    )

    for ext in ["png", "jpg", "svg"]:
        cover_filename = "cover.%s" % ext
        if os.path.exists(cover_filename):
            break
        else:
            cover_filename = None

    if cover_filename:
        args.append("--cover=%s" % cover_filename)
        if not options['stretch cover image']:
            args.append("--preserve-cover-aspect-ratio")

    for i in ['top', 'left', 'right', 'bottom']:
        if options['margin'][i] is not None:
            args.append("--margin-%s" % i)
            args.append(str(options['margin'][i]))

    shell.run(" ".join(args), shell=True)
    #shell.save_output(args, "%s.html" % options['filename'])
