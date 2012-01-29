"""Use Pandoc and Calibre to compile Markdown text to Epub, with source included in the Epub."""

import logging
import sys
import yaml
import mdepub
import mdepub.actions

def main():
    log = logging.getLogger('__main__')

    mdepub.init()

    log.debug("Arguments: %s", repr(mdepub.arguments))

    for action in mdepub.arguments.action:
        getattr(mdepub.actions, action).run()

if __name__ == '__main__':
    main()
