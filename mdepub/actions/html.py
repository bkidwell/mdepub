import logging
import mdepub
from mdepub import shell
import os
from mdepub import options
from mdepub import project_path
from BeautifulSoup import BeautifulSoup
from mdepub.filename import getFN

log = logging.getLogger('html')

def checkForBadLinks(html):
    soup = BeautifulSoup(html)

    ids = [tag['id'] for tag in soup.findAll(id=True)]
    ids.extend([tag['name'] for tag in soup.findAll( attrs={'name': True} )])

    for tag in soup.findAll(href=True):
        href = tag['href']
        if href[:1] == u'#':
            if href[1:] not in ids:
                log.warn("Internal link points to non-existent target '{}'".format(href))

def run():
    log.debug("run()")

    os.chdir(project_path)

    css_file = getFN("css")

    args = ["pandoc", "--standalone", "--email-obfuscation=none"]

    if os.path.exists(css_file):
        args.extend(["-c", css_file])
    if options['smart quotes']:
        args.append("--smart")
    args.append(getFN("md"))

    html = shell.pipe(args, None)

    checkForBadLinks(html)

    with file(getFN("html"), 'w') as f:
        f.write(html)
