# mdepub: Help for options.yaml

This file lists the options found in an mdepub `options.yaml` file.


title

:   Title of the ebook.

title sort

:   The value used to sort the title in a database, for example `title sort` for "The Giver" would be "Giver, The". Specify a null value (the single character "~") if it would be the same as `title`.

authors

:   Comma or semicolon separated list of authors.

author sort

:   Usually "Lastname, Firstname" of the first author, or "~" to copy the `authors` field.

publication date

:   Date the source material was published, in the format "D MMM YYYY".

publisher

:   Name of the publisher.

book producer

:   Who produced this Epub file.

isbn

:   Any relevant ISBN number that may appy, or "~" for none.

language

:   Primary language of this ebook.

rating

:   Your personal rating, which will be imported into Calibre. "~" or 1 through 5.

series

:   Name of the series this ebook belongs to or "~" for none.

series index

:   Book number within the series or "~" for none.

uuid

:   The UUID of this Epub file. mdepub automatically gives each new project a random UUID.

tags

:   A comma-separated list of tags that can help you browse your ebook collection in a tool like Calibre, or "~" for no tags. The list must begin and end with square brackets, and each tag should be a single word. Use hyphens instead of spaces for multiple-word tags. Example:

        [fiction, historical-fiction, boston]

filename

:   Customize the MD, HTML, CSS, and EPUB filenames, or "~" for default, based on `title.

description

:   Enter the book description here, in Markdown syntax. Yaml allows long, multiple-paragraph strings by prefixing the string with a "|" and then prefixing each line of the string with at least one space. Example:

        description: |
          This is the first paragraph of the book description.

          This is another paragraph.

smart quotes

:   Automatically convert `'` and `"` to proper left and right quote marks, and also handle dashes and ellipses; `true` or `false`. Turn this off if it doesn't work correctly for your source material.

stretch cover image

:   Distort cover image to fill entire screen; `true` or `false`. The default `false` fills the screen with the cover but adds white bars to prevent stretching of the image.

chapter head level

:  Lowest chapter heading level to include in the table of contents. For example, `2` will include the title H1, and only H2 level chapter headings. `3` would additionally include section-level H3s that appear under chapter H2s.

margin

:   A dictionary of four named values, `top`, `left`, `right`, and `bottom`. Null "~" values mean to use Calibre's defaults. I prefer left and right margins of `8`, so I hard-coded those values into the mdepub project template.
