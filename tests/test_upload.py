#!/usr/bin/env python

import subprocess
import glob

def test_push():
    for fname in glob.glob("*.xml"):
        proc = subprocess.Popen([
                        "taxii-push", 
                        "--path", "http://localhost:9000/services/inbox", 
                        "-f", fname, 
                        "--dest", "collection", 
                        "--username", "travis", 
                        "--password", "travis"
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )

        out,err = proc.communicate()
        print(out)
        assert("Content block successfully pushed" in out.decode("utf-8"))