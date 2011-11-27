import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path
from mdepub import arguments
from zipfile import ZipFile
from BeautifulSoup import BeautifulSoup

log = logging.getLogger('epub')

def quote(text):
    return text.replace('"', '\'')

def run():
    log.debug("run()")

    os.chdir(project_path)

    # Get source and dest file times

    time = {}
    for ext in ['md', 'css', 'html', 'zip']:
        f = "%s.%s" % (options['filename'], ext)
        if os.path.exists(f):
            time[ext] = os.path.getmtime(f)
        else:
            time[ext] = None

    if time['html'] < time['md'] or time['html'] < time['css']:
        mdepub.actions.html.run()
        time['html'] = os.path.getmtime("%s.html" % options['filename'])
    if time['zip'] < time['html']:
        mdepub.actions.archive.run()

    # Get description html from markdown

    description = shell.pipe(["pandoc"], options['description'])

    # Setup ebook-convert args

    args = [
        "ebook-convert",
        "\"%s.html\"" % options['filename'],
        "\"%s.epub\"" % options['filename'],
        "--authors=\"%s\"" % quote(options['authors']),
        "--author-sort=\"%s\"" % quote(options['author sort']),
        "--pubdate=\"%s\"" % options['publication date'],
        "--title=\"%s\"" % quote(options['title']),
        "--tags=\"%s\"" % quote(','.join(options['tags'])),
        "--comments=\"%s\"" % quote(description)
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

    # Run ebook-convert

    shell.run(" ".join(args), shell=True)
    #shell.save_output(args, "%s.html" % options['filename'])

    # Add source zip file to epub and update content.opf with correct uuid

    metadata = None
    with ZipFile("%s.epub" % options['filename'], 'a') as zip:
        if arguments.source:
            zip.write("%s.zip" % options['filename'], "META-INF/source.mdepub.zip")
        metadata = zip.read("content.opf")
    shell.run(["zip", "-d", "%s.epub" % options['filename'], "content.opf"])
    with ZipFile("%s.epub" % options['filename'], 'a') as zip:
        #metadata = zip.read("content.opf")
        soup = BeautifulSoup(metadata)
        id = soup.find(id="uuid_id")
        id.contents[0].replaceWith(options['uuid'])
        print soup
        zip.writestr("content.opf", str(soup))

#TODO: series, series-index
#TODO: publisher
#TODO: language
#TODO: rating
