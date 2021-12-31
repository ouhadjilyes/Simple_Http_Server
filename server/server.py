from http.server import HTTPServer, BaseHTTPRequestHandler
import time


class MyHttp(BaseHTTPRequestHandler):

    def do_GET(self):

        #try:
            #with open('index.html','rb') as f:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Http Server is Running.....</h1></body></html>", "utf-8"))

        #except IOError:
            #self.send_error(404, 'File Not Found: %s' % self.path)
        
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date +  '"}' , "utf-8"))


if __name__ == "__main__":
    server = HTTPServer(('localhost', 4444), MyHttp)
    print("Server is running on localhost 4444 ....")
    server.serve_forever()
    server.server_close()
    print("Server down!")
