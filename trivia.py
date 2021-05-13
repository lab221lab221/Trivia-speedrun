import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import random

ip = str(socket.gethostbyname(socket.gethostname()))

questions_file = open("trivia.json", "r")
line = ""
for i in questions_file.readlines():
    line += i
questions = json.loads(line)
questions_file.close()
#print(questions)

class Trivia_Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/" or self.path == "/login":
            try:
                self.send_response(200)
                self.end_headers()

                self.send_header("Content-type", "text/html")
                file = open("trivia.html", "r")
                html = ""
                for i in file.readlines():
                    html += i
                self.wfile.write(bytes(html, "utf-8"))
            except Exception as e:
                print(e)
        elif self.path == "/trivia.css":
            try:
                self.send_response(200)
                self.end_headers()
                file_css = open("trivia.css", "r")
                css = ""
                for i in file_css.readlines():
                    css += i
                self.wfile.write(bytes(css, "utf-8"))
            except Exception as e:
                print(e)
        elif self.path == "/trivia_questions":
            try:
                self.send_response(200)
                self.end_headers()

                self.send_header("Content-type", "text/html")
                file = open("trivia_questions.html", "r")
                html = ""
                for i in file.readlines():
                    html += i
                self.wfile.write(bytes(html, "utf-8"))
            except Exception as e:
                print(e)
        elif self.path == "/questions":
            try:
                self.send_response(200)
                self.end_headers()
                
                self.send_header("Content-type", "application/json")
                json_obj = random.choice(questions["questions"])
                self.wfile.write(bytes(json.dumps(json_obj), "utf-8"))
            except Exception as e:
                print(e)

try:
    webServer = HTTPServer((ip, 8080), Trivia_Server)
    print("Server started http://%s:%s" % (ip, 8080))
    webServer.serve_forever()
except Exception as e:
    webServer.server_close()
    print("Server stopped.")
    print(e)
