# Pandoc Markdown Cheat Sheet

<style>
pre {
	margin: 1em;
}
</style>

## Title Blocks

	% title
	% author(s) (separated by semicolons)
	% date

## Headers

	# H1 -- first one will be inserted from title automatically
	## H2
	### H3
	etc.

## Block elements

	> blockquote
	> ...

	* Unordered lists use *, -, or +
	* ...

	1. Ordered lists use a number followed by a period.
	2. ...

		Code blocks are indented by a tab or 4 spaces...

	~~~
	or begin and end with a line of 3 or more ~ characters.
	~~~

	---
	An HR is a line of 3 or more -, *, or _ optionally alternating with spaces.

	![An image with alt text by itself becomes a captioned figure](/url/of/image.png)

## Span elements

	This is [an example](http://example.com/ "Title") inline link.
	[This link](http://example.net/) has no title attribute.
	Simple link: <http://example.com/>

	![Alt text](/path/to/img.jpg)
	![Alt text](/path/to/img.jpg "Optional title")

	*em* _em_ **strong** __strong__

	`inline cocde`
	``inline code with ` in it``

	Backslash escape: \(
	Line break: \
	(backslash at end of line)

	H~2~O is a liquid.  2^10^ is 1024.
	~subscript\ text~ ^superscript\ text^
	~~strikeout~~

	$latex math notation$

## Definition Lists

	Term 1

	:   Definition 1

	Term 2 with *inline markup*

	:   Definition 2

	    { some code, part of Definition 2 }

	    Third paragraph of definition 2.

	Term 1
	  ~ Definition 1
	Term 2
	  ~ Definition 2a
	  ~ Definition 2b

## Footnotes

	Here is a footnote reference,[^1] and another.[^longnote]

	[^1]: Here is the footnote.

	[^longnote]: Here's one with multiple blocks.

		Subsequent paragraphs are indented to show that they
	belong to the previous footnote.

			{ some.code }

		The whole paragraph can be indented, or just the first
		line.  In this way, multi-paragraph footnotes work like
		multi-paragraph list items.

	This paragraph won't be part of the note, because it isn't indented.

## Tables

Simple table:

	  Right     Left     Center     Default
	-------     ------ ----------   -------
	     12     12        12            12
	    123     123       123          123
	      1     1          1             1

	Table: Caption begins with "Table:" or ":"

No column headers:

	-------     ------ ----------   -------
	     12     12        12             12
	    123     123       123           123
	      1     1          1              1
	-------     ------ ----------   -------

Borders:

	: Sample grid table.

	+---------------+---------------+--------------------+
	| Fruit         | Price         | Advantages         |
	+===============+===============+====================+
	| Bananas       | $1.34         | - built-in wrapper |
	|               |               | - bright color     |
	+---------------+---------------+--------------------+
	| Oranges       | $2.10         | - cures scurvy     |
	|               |               | - tasty            |
	+---------------+---------------+--------------------+

## Command Line Help

<pre>pandoc [OPTIONS] [FILES]
Input formats:  native, markdown, markdown+lhs, rst, rst+lhs, html, latex,
  latex+lhs
Output formats:  native, html, html+lhs, s5, slidy, docbook, opendocument, odt,
  epub, latex, latex+lhs, context, texinfo, man, markdown, markdown+lhs, plain,
  rst, rst+lhs, mediawiki, rtf
Options:
  -f FORMAT, -r FORMAT  --from=FORMAT, --read=FORMAT
  -t FORMAT, -w FORMAT  --to=FORMAT, --write=FORMAT
  -s                    --standalone
  -o FILENAME           --output=FILENAME
  -p                    --preserve-tabs
                        --tab-stop=TABSTOP
                        --strict
                        --reference-links
  -R                    --parse-raw
  -S                    --smart
  -m[URL]               --latexmathml[=URL], --asciimathml[=URL]
                        --mathml[=URL]
                        --mimetex[=URL]
                        --webtex[=URL]
                        --jsmath[=URL]
                        --gladtex
  -i                    --incremental
                        --offline
                        --xetex
  -N                    --number-sections
                        --section-divs
                        --no-wrap
                        --sanitize-html
                        --email-obfuscation=none|javascript|references
                        --id-prefix=STRING
                        --indented-code-classes=STRING
                        --toc, --table-of-contents
                        --base-header-level=LEVEL
                        --template=FILENAME
  -V FILENAME           --variable=FILENAME
  -c URL                --css=URL
  -H FILENAME           --include-in-header=FILENAME
  -B FILENAME           --include-before-body=FILENAME
  -A FILENAME           --include-after-body=FILENAME
  -C FILENAME           --custom-header=FILENAME
  -T STRING             --title-prefix=STRING
                        --reference-odt=FILENAME
                        --epub-stylesheet=FILENAME
                        --epub-metadata=FILENAME
  -D FORMAT             --print-default-template=FORMAT
                        --data-dir=DIRECTORY
                        --dump-args
                        --ignore-args
  -v                    --version
  -h                    --help</pre>
