#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from os import path
from time import sleep
import random

import display

class handler(BaseHTTPRequestHandler):
    root_dir = path.abspath(path.dirname(__file__))

    def do_GET(self):
        logging.info("GET")
        file_path = path.join(self.root_dir, 'index.html')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', path.getsize(file_path))
        self.end_headers()
        with open(file_path, mode='r', encoding='utf-8') as f:
            content = f.read()
            self.wfile.write(content.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        logging.info("POST: path: %s, data: %s", self.path, post_data)

        bad_request = True

        if self.path == '/char':
            display.write_char(post_data)
            bad_request = False 

        if self.path == '/segment':
            display.flip_segment(post_data)
            bad_request = False

        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf8')
        self.end_headers()
        response = '{"result": "OK"}'
        if bad_request:
            response = '{"result": "BAD REQUEST"}'
        self.wfile.write(response.encode('utf-8'))



def run(server_class=HTTPServer, handler_class=handler, port=8080):
    display.init()
    for c in '987654321 ':
        display.write_char(c)
        sleep(0.25)
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('listening on port ...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('stopping...\n')
