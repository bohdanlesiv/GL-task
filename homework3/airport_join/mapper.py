#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    iata_code = -1
    iata_name = -1
    iata_code2 = -1
    avg = -1

    if len(line) == 2:
       iata_code = line[0]
       avg = line[1]
    else:
       iata_code2 = line[0]
       iata_name = line[1]

    print '%s,%s,%s,%s' % (iata_code,iata_name,iata_code2,avg)