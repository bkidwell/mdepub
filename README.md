# Markdown Epub Builder

`mdepub` is a tool which allows you to compose a book in Markdown format
and use Pandoc and Calibre to compile an Epub package including all of
the book's source material. In effect you can keep the source and
product in the same file in your library; if you ever want to revise the
product, you merely need to extract the source, make edits, and
recompile.

**This program is a work in progress. It's not fully functional yet!**

## Requirements

* argparse -- Python command line argument parser
* Beautiful Soup -- HTML/XML stream parsing and manipulation for Python
* Calibre (Calibre's `ebook-convert` command is used to manipulate and
  build EPUB package files.)
* pandoc -- all purpose converter to and from Markdown syntax
* Python 2.7
* YAML for Python -- minimal config / serialization syntax
