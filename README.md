# Markdown Epub Builder

`mdepub` is a tool which allows you to compose a book in Markdown format
and use Pandoc and Calibre to compile an Epub package including all of
the book's source material. In effect you can keep the source and
product in the same file in your library; if you ever want to revise the
product, you merely need to extract the source, make edits, and
recompile.

**This program is a work in progress. It's not fully functional yet!**

## Requirements

* Beautiful Soup -- HTML/XML stream parsing and manipulation for Python
* Calibre (Calibre's `ebook-convert` command is used to manipulate and
  build EPUB package files.)
* pandoc -- all purpose converter to and from Markdown syntax
* Python 2.7
* YAML for Python -- minimal config / serialization syntax

Install Calibre on a Unix box:

    sudo python -c "import sys; py3 = sys.version_info[0] > 2; u = __import__('urllib.request' if py3 else 'urllib', fromlist=1); exec(u.urlopen('http://status.calibre-ebook.com/linux_installer').read()); main()"

Ubuntu packages for the rest of the requirements:

    sudo apt-get install pandoc python-beautifulsoup python-yaml
