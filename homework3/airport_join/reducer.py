#!/usr/bin/env python
import sys

avg_dict = {}
airports_name_dict ={}

for line in sys.stdin:
    line = line.strip()
    iata_code, iata_name, iata_code2, avg = line.split(',')


    if iata_code == '-1':
       airports_name_dict[iata_code2] = iata_name
    else:
       avg_dict[iata_code] = avg


for iata_code in avg_dict.keys():
    print '%s,%s,%s' % (iata_code, airports_name_dict[iata_code], avg_dict[iata_code])




