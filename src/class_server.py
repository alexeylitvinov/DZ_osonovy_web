from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    def __get_html_content(self):
        with open('index.html', encoding='utf8') as file:
            self.data = file.read()
        return self.data

    def do_GET(self):
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))
