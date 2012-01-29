"""Module for handling mdepub command line arguments."""

import argparse
import logging
import textwrap
import mdepub

log = logging.getLogger('argumentparser')

help="""\
Use Pandoc and Calibre to compile Markdown text to Epub, with source
included in the Epub.
"""

epilog="""\
actions:
  create       Create empty project in this folder
  html         Translate Markdown text to html
  archive      Archive source files to zip file
  epub         Convert HTML to Epub and include source zip file
  extract      Extract the source files from the given Epub file
  clean        Delete output files except Epub package
  newid        Assign a new ID for this project in options.yaml
  version      Print mdepub version number

required files:
  options.yaml  Project options
  $filename.md  Book text in Markdown format

option files:
  cover.[png|jpg|svg]  Cover image
  $filename.css        CSS stylesheet

output files:
  $filename.html  Book text in HTML format
  $filename.epub  Complete Epub package
  source.zip      All the files in the project except output files

When performing the 'epub' step, 'html' and 'archive' are also
automatically executed if $base_filename.md has a newer date than the
respective output files.
"""

def setup_args(parser):
    """Add mdepub argument structure to an instance of ArgumentParser."""

    parser.add_argument(
        'action', nargs='+', metavar='action',
        choices=['create', 'html', 'archive', 'epub', 'extract',
        'clean', 'newid', 'version'],
        help="Which action to perform."
    )
    parser.add_argument(
        '--nosource', help="Don't include source zip in epub file",
        action='store_const', dest='source', const=False, default=True
    )
    parser.add_argument(
        '--filename', help="Base filename for project files, when \
        creating a new project or to override the value in options.yaml"
    )
    parser.add_argument(
        '--from', help="Path to Epub file for 'extract' action", dest='fromfile'
    )
    parser.add_argument(
        '--to', help="Path for 'extract' or 'fromcalibre' actions to extract\
        Epub source files to (defaults to a subfolder of the current path)", dest='to'
    )

class ArgumentParser(argparse.ArgumentParser):
    """Extend argparse.ArgumentParser with the argument structure for mdepub."""

    def __init__(self):
        super(ArgumentParser, self).__init__(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=help, epilog=epilog, prog=mdepub.PROGRAM_NAME
        )
        setup_args(self)
