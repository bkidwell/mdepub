"""Translate Markdown text to html."""

from BeautifulSoup import BeautifulSoup
import logging
import os
import os.path
import sys
import mdepub
from mdepub import shell
from mdepub.filename import getFN

log = logging.getLogger('html')

def checkForBadLinks(html):
    """Find all internal bookmarks pointed to by hrefs in html, and make sure they are valid."""

    soup = BeautifulSoup(html)

    ids = [tag['id'] for tag in soup.findAll(id=True)]
    ids.extend([tag['name'] for tag in soup.findAll( attrs={'name': True} )])

    for tag in soup.findAll(href=True):
        href = tag['href']
        if href[:1] == u'#':
            if href[1:] not in ids:
                log.warn("Internal link points to non-existent target '{}'".format(href))

def run():
    """Run this action."""

    options = mdepub.options
    project_path = mdepub.project_path

    log.debug("run()")
    mdepub.require_opts_file()

    os.chdir(project_path)

    css_file = getFN("css")

    args = ["pandoc", "--standalone", "--email-obfuscation=none"]

    src = getFN("md")
    if not os.path.exists(src):
        log.fatal("\"%s\" not found.", src)
        sys.exit(1)

    if os.path.exists(css_file):
        args.extend(["-c", css_file])
    if options['smart quotes']:
        args.append("--smart")
    args.append(src)

    html = shell.pipe(args, None)

    checkForBadLinks(html)

    with file(getFN("html"), 'w') as f:
        f.write(html)
