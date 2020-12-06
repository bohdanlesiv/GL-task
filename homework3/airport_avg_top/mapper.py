#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    try:
       airline_code =  line[8]
       depature_delay = int(line[11])
    except Exception:
        pass
    else:
       if depature_delay is not None:
           print '%s,%s' % (airline_code, depature_delay)
