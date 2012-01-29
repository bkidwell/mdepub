#!/bin/bash

d=`dirname $0`
d=`readlink -f $d/..`

pushd $d >/dev/null

pandoc README.md>README.html
pandoc doc/options.md>doc/options.html
pandoc doc/pandoc_markdown.md>doc/pandoc_markdown.html

popd >/dev/null