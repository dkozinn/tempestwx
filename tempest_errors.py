#!/usr/bin/python

import csv
import sys

# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

errors=["none",
        "Lightning failed",
        "Lightning noise",
        "Lightning disturber",
        "Pressure",
        "Temperature",
        "RH",
        "Wind",
        "Precipitation",
        "Light/UV"
        ]

def main():
        if len(sys.argv) != 3:
                print("Usage: python tempest_errors.py [sensor_status] [sensor_errors]")
                sys.exit(1)
                
        infile = sys.stdin
        #infile=open('in.csv',newline='')
        outfile = sys.stdout

        df = open('debug.log',
        r = csv.DictReader(infile)
        header = r.fieldnames

        w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
        w.writeheader()

        for error_val in r:
                curError=int(error_val['sensor_status'])
                sensor_errors=""
                for i in (range(0,len(errors)-1)):
                        if testBit(curError,i):
                                if len(sensor_errors)>0:
                                        sensor_errors=sensor_errors+","
                                sensor_errors = sensor_errors+errors[i+1]

                error_val['sensor_errors']=sensor_errors
                w.writerow(error_val)

main()