#!/usr/bin/env python

import subprocess
import time
import os
import signal

proc = subprocess.Popen(['rstserv', 'README.rst'])
time.sleep(1)
ret = proc.poll()
if ret is not None:
    raise RuntimeError('cannot start server, return code is %d' % ret)

try:
    ret = subprocess.call(['curl', 'http://127.0.0.1:8080/'])
    if ret != 0:
        raise RuntimeError('curl returns %d' % ret)

finally:
    os.kill(proc.pid, signal.SIGKILL)
