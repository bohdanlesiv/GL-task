#!/usr/bin/env python
import sys
from heapq import nlargest

airport_delay = {}
airport_delay_avg = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    airline_code, depature_delay = line.split(',')

    if airline_code in airport_delay:
        airport_delay[airline_code].append(int(depature_delay))
    else:
        airport_delay[airline_code] = []
        airport_delay[airline_code].append(int(depature_delay))

#Reducer
for airline_code in airport_delay.keys():
    depature_delay_avg = sum(airport_delay[airline_code])*1.0 / len(airport_delay[airline_code])
    airport_delay_avg[airline_code] = []
    airport_delay_avg[airline_code].append(depature_delay_avg)


top_5 = nlargest(5 ,airport_delay_avg, key=airport_delay_avg.get)


for airline_code in top_5:
    print '%s,%s' % (airline_code, str(airport_delay_avg[airline_code][0]))




