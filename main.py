import http.server
import socketserver

import menu


def webServer():
    hostname = input("Enter hostname: ");
    PORT = 8000;
    Handler = http.server.SimpleHTTPRequestHandler;
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
    httpd.serve_forever()

#menu.MainMenu.consoleMenu()
menu.MainMenu.router()