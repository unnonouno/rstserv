import argparse
import imp
import os
import socket
import sys

from rstserv import __version__

if sys.version_info >= (3, 0):
    from http.server import BaseHTTPRequestHandler
    from http.server import HTTPServer
else:
    from BaseHTTPServer import BaseHTTPRequestHandler
    from BaseHTTPServer import HTTPServer

from docutils.core import publish_parts
from docutils.writers.html4css1 import Writer

try:
    import markdown
except:
    markdown = None

import rstserv

def read_all(path):
    f = open(path)
    try:
        return f.read()
    finally:
        f.close()


def rst2html(file_path):
    string = read_all(file_path)
    w = Writer()
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
            if markdown and path.endswith('.md'):
                html = md2html(path)
            else:
                html = rst2html(path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(html)
            return

    try:
        host = socket.gethostname()
        server = HTTPServer(('', args.port), MyHandler)
        print('rstserv %s' % __version__)
        print('Access http://%s:%i' % (host, args.port))
        print('Type <Ctrl-C> to stop the server')
        server.serve_forever()

    except Exception:
        e = sys.exc_info()[1]
        sys.stderr.write(str(e))
        sys.stderr.write('\n')
        sys.exit(1)
