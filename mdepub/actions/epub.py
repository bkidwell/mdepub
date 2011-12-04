import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path
from mdepub import arguments
from zipfile import ZipFile
from BeautifulSoup import BeautifulSoup
from mdepub.filename import getFN
import uuid

log = logging.getLogger('epub')

def quote(text):
    return text.replace('"', '\'')

def run():
    log.debug("run()")

    os.chdir(project_path)

    # Get source and dest file times

    time = {}
    for ext in ['md', 'css', 'html', 'zip']:
        f = getFN(ext)
        if os.path.exists(f):
            time[ext] = os.path.getmtime(f)
        else:
            time[ext] = None

    if time['html'] < time['md'] or time['html'] < time['css']:
        mdepub.actions.html.run()
        time['html'] = os.path.getmtime(getFN("html"))
    if time['zip'] < time['html']:
        mdepub.actions.archive.run()

    # Get description html from markdown

    if 'description' in options:
        description = shell.pipe(["pandoc"], options['description'])
    else:
        description = ""

    # Setup ebook-convert args

    if not 'title' in options: raise "No title given in options.yaml"
    args = [
        "ebook-convert",
        '"' + getFN("html") + '"',
        '"' + getFN("epub") + '"',
        "--title=\"{}\"".format(quote(options['title']))
    ]
    for a, b in (
        ('author-sort',   'author sort'),
        ('authors',       'authors'),
        ('book-producer', 'book producer'),
        ('isbn',          'isbn'),
        ('language',      'language'),
        ('pubdate',       'publication date'),
        ('publisher',     'publisher'),
        ('rating',        'rating'),
        ('series',        'series'),
        ('series-index',  'series index'),
        ('title-sort',    'title sort'),
    ):
        if options.get(b): args.append("--{}=\"{}\"".format(a, quote(options[b])))

    if options.get("tags"):
        args.append(  "--tags=\"{}\"".format(quote(','.join(options['tags'])))  )

    args.append("--chapter=\"//h:h{}\"".format(options.get('chapter head level') or 2))
    tmp = []
    for i in range(options.get('chapter head level') or 2):
        if len(tmp) > 0: tmp.append("or")
        tmp.append("name()='h{}'".format(str(i + 1)))
    args.append(
        "--level1-toc=\"//*[{}]\"".format(" ".join(tmp))
    )

    for ext in ["png", "jpg", "svg"]:
        cover_filename = "cover.{}".format(ext)
        if os.path.exists(cover_filename):
            break
        else:
            cover_filename = None

    if cover_filename:
        args.append("--cover=\"{}\"".format(cover_filename))
        if not options.get('stretch cover image'):
            args.append("--preserve-cover-aspect-ratio")

    if options.get('margin'):
        for i in ['top', 'left', 'right', 'bottom']:
            if options['margin'].get(i) is not None:
                args.append("--margin-{}".format(i))
                args.append(str(options['margin'][i]))

    # Run ebook-convert

    shell.run(" ".join(args), shell=True)

    # Add source zip file to epub and update content.opf with correct uuid

    metadata = None
    with ZipFile(getFN("epub"), 'a') as zip:
        if arguments.source:
            zip.write(getFN("zip"), "META-INF/source.mdepub.zip")
        metadata = zip.read("content.opf")
    shell.run(["zip", "-d", getFN("epub"), "content.opf"])
    with ZipFile(getFN("epub"), 'a') as zip:
        #metadata = zip.read("content.opf")
        soup = BeautifulSoup(metadata)
        id = soup.find(id="uuid_id")
        id.contents[0].replaceWith(options.get('uuid') or mdepub.new_id())
        #print soup
        zip.writestr("content.opf", str(soup))
