# Markdown Epub Builder


`mdepub` is a tool which allows you to compose a book in Markdown format
and use Pandoc and Calibre to compile an Epub package including all of
the book's source material. In effect you can keep the source and
product in the same file in your library; if you ever want to revise the
product, you merely need to extract the source, make edits, and
recompile.

    Markdown sourcecode --> | Epub file:            |
                            |   * validated XHTML   |
                            |   * metadata          |
                            |   * Markdown sourcode |


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


## Installation


No installation script is provided. The simplest way to install mdepub
is to download the source as a `.zip` or `.tar.gz`, or `git clone`. Put
the package files in `~/Apps/mdepub` and then do this:

    chmod +x ~/Apps/mdepub/__main__.py
    ln --symbolic ~/Apps/mdepub/__main.py__ ~/bin/mdepub

(Make sure `~/bin` is in your `$PATH` variable when you run `mdepub`.)


### Windows


`mdepub` should work in Windows as well. Make sure all your requirements
are installed and make sure you can run `python`, `pandoc`, and
`ebook-convert` by just calling their name from the command line. (You
probably will have to edit your `$PATH` environment variable.)

To invoke `mdepub`, you can either do

    python -m [path to...]\mdepub.zip [mdepub arguments]

Or create a batch file in your `$PATH` that calls Python in this way and
passes command line arguments through to mdepub.


## Usage


**Create an empty Epub project**:

    mdepub create
    # Interactively enter Title, Author(s), and project directory ("." default).

The `create` command copies boilerplate code into `$title.md`,
`$title.css`, and `options.yaml` in the project directory.

**Compile ebook project into HTML** (good for quick
preview):

    mdepub html

**Compile ebook project into Epub**:

    mdepub epub

All source files in the project directory are included in the Epub
package as `META-INF/source.mdepub.zip`.

**Delete derived files** (html, epub) leaving only source:

    mdepub clean

**Extract an existing mdepub Epub file's source** into a directory under
the current directory (so you can edit and repackage it):

    mdepub extract ~/Path/Filename.epub

**Get all command line help**:

    mdepub --help


## Starting Your Markdown Source File


Metadata for the compiled Epub file is specified in `options.yaml`. See
`doc/options.html` for details.

mdepub assumes the entire ebook source text is contained in a single
`.md`. Stylesheet information is given in a `.css` file with the same
name. Any attached images can be included in an `images/` subdirectory
in your project; be sure you link to the images in your source using
relative paths, for example `images/author.jpg`.

mdepub uses Pandoc to convert Markdown syntax to strict XHTML. If you
are not familiar with Markdown, see the cheat sheet in
`doc/pandoc_markdown.html`.

If you're starting a project from text that's already in a computer file
or files, it's a good idea to include that in your project in an
`upstream` directory. In case you ever have to refer back to it, this
directory will be included in the `source.mdepub.zip` along with all
other project files when you compile the Epub file. If your source is in
a format that Pandoc can read, such as HTML, you can use Pandoc to
convert it to Markdown to get you started. See
[Pandoc's User Guide](http://johnmacfarlane.net/pandoc/README.html) for
details.

**Headings:** There should only be one H1 (denoted by a single `#` in Markdown) in
your source file; this is the title of the book. Front matter should be
placed before the first chapter heading (`##`).

**Page breaks:** Each chapter will start with a page break. Additional
page breaks can be added by wrapping a block of text in

    <div class="break">
    </div>

**Internal hyperlinks:** Hyperlinks to named sections follow the
Pandoc's rules for HTML names of sections (see Pandoc's User Guide). For
example, to link to a chapter named "Chapter III A Caucus-Race and a
Long Tale", write:

    [A Caucus-Race and a Long Tale](#chapter-iii-a-caucus-race-and-a-long-tale)

Check out the sample *Alice in Wonderland* project in mdepub's
`sample` directory for specific examples of use of Pandoc's Markdown and
mdepub's stylesheet to lay out an ebook.
