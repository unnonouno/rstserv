#!/usr/bin/env python

import subprocess
import time

proc = subprocess.Popen('rstserv README.rst', shell=True)
time.sleep(1)
try:
    subprocess.check_call(['curl', 'http://127.0.0.1:8080/'])
finally:
    proc.kill()

