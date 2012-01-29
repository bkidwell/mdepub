#!/bin/bash

d=`dirname $0`
d=`readlink -f $d/..`

pushd $d >/dev/null

pandoc --standalone README.md>README.html
pandoc --standalone doc/options.md>doc/options.html
pandoc --standalone doc/pandoc_markdown.md>doc/pandoc_markdown.html

popd >/dev/null