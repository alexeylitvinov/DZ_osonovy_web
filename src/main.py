from http.server import HTTPServer
from class_server import MyServer

host_name = 'localhost'
server_port = 8080


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), MyServer)
    print('Server started http://%s:%s' % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('server stopped')
