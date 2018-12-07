from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import subprocess



class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def call_meme_program(self, text_top, text_bottom):
        p = subprocess.Popen(["meme img.jpg {} {} -o font_bgr '[255,255,255]' -o opencv_font '0' -o opencv_font_thickness '6'".format(text_top, text_bottom)], bufsize=2048, shell=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
        p.wait()


    def get_meme_img(self):
        print(self.path)
        url = self.path
        parsed = urlparse.urlsplit(url)
        query = urlparse.parse_qs(parsed.query)
        top = query['top'][0] if 'top' in query else None
        bottom = query['bottom'][0] if 'bottom' in query else None
        if top and bottom:
            self.call_meme_program(top, bottom)
        with open('img-meme.jpg', 'rb') as file:
            return file.read()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "image/jpeg")
        self.end_headers()
        self.wfile.write(self.get_meme_img())


httpd = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()