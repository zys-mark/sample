#!/usr/bin/env python
import time
import sys
import os
import json

def main(args):
    if "timeout" in args:
        count = 1
        while True:
            #print "sleepin till i die (%s)" % count
            time.sleep(10)
            count += 1

    exit_code = 0
    if "pass" in args:
        exit_code = 0
        print "This task is going to pass."

    if "fail" in args:
        exit_code = 1
        print "This task is going to FAIL."

    if "results" in args:
        json_out = open('results.json', 'w')
        out_results = {
                "results":[
                    {
                        "status":"pass",
                        "test_file":"test_1",
                        "url":"http://buildlogs.mongodb.org/build/535fba25d2a60f3135000ae7/test/535fba25d2a60f32300000b7/",
                        "exit_code":0,
                        "elapsed":0.32200002670288086,
                        "start":1398782500.359,
                        "end":1398782500.681
                        },
                    {
                        "status":"pass",
                        "test_file":"test_2",
                        "url":"http://buildlogs.mongodb.org/build/535fba25d2a60f3135000ae7/test/535fba25d2a60f320c000127/",
                        "exit_code":0,
                        "elapsed":0.16000008583068848,
                        "start":1398782500.681,
                        "end":1398782500.841
                        },
                    {
                        "status":"fail",
                        "test_file":"test_3",
                        "url":"http://buildlogs.mongodb.org/build/535fba25d2a60f3135000ae7/test/535fba25d2a60f320c000128/",
                        "exit_code":0,
                        "elapsed":0.1679999828338623,
                        "start":1398782500.841,
                        "end":1398782501.009
                        },
                    ]
                }
        json.dump(out_results, json_out)
    sys.exit(exit_code)

if __name__ == "__main__":
    main(sys.argv[1:])
