#!/usr/bin/env python

import logging
import mdepub
import yaml
import mdepub.actions
import sys

log = logging.getLogger('main')

log.debug("Arguments: %s", repr(mdepub.arguments))

for action in mdepub.arguments.action:
    getattr(mdepub.actions, action).run()
