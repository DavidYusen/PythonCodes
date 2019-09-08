from wsgiref.simple_server import make_server
from hello import applicaton

httpd = make_server('', 8000, applicaton)
print('Serving HTTP on port 8000...')
httpd.serve_forever()