'''
Copyright (c) 2011, Yuya Unno
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Yuya Unno nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import argparse
import imp
import os
import socket
import sys

if sys.version_info >= (3, 0):
    from http.server import BaseHTTPRequestHandler
    from http.server import HTTPServer
else:
    from BaseHTTPServer import BaseHTTPRequestHandler
    from BaseHTTPServer import HTTPServer

from docutils.core import publish_parts
from docutils.writers.html4css1 import Writer


def read_all(path):
    with open(path) as f:
        return f.read()


def rst2html(file_path):
    string = read_all(file_path)
    w = Writer()
    import rstserv
    (_, path, _) = imp.find_module('template', rstserv.__path__)
    overrides = {
        'stylesheet': os.path.join(path, 'default.css'),
        'stylesheet_path': None,
        'initial_header_level': 2
        }
    r = publish_parts(string, writer=w, settings_overrides=overrides)
    result = r['whole']
    return result.encode('utf-8')


def md2html(file_path):
    import markdown
    source = read_all(file_path).decode('utf-8')
    body = markdown.markdown(source)
    html = '<html><body>\n' + body + '</body></html>\n'
    return body


def parse_args():
    p = argparse.ArgumentParser(
        description='rst server')
    p.add_argument('-p', '--port', default=8080,
                   type=int, help='port number')
    p.add_argument('file', metavar='FILE', help='rst file to show')
    return p.parse_args()


def main():
    args = parse_args()
    path = args.file

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if path.endswith('.md'):
                html = md2html(path)
            else:
                html = rst2html(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(html)
            return

    host = socket.gethostname()
    server = HTTPServer(('', args.port), MyHandler)
    print('Access http://%s:%i' % (host, args.port))
    print('Type <Ctrl-C> to stop the server')
    server.serve_forever()
