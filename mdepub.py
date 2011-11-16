#!/usr/bin/env python

import logging
import mdepub
import yaml
import mdepub.actions

log = logging.getLogger('main')

#print yaml.dump(mdepub.arguments)
log.debug("Arguments: %s", repr(mdepub.arguments))

for action in mdepub.arguments.action:
    getattr(mdepub.actions, action).run()
