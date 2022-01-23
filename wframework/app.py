from .utils import *


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']
        data = parse_data(environ)
        if path[-1] != '/':
            path += '/'
        if path in self.routes:
            controller = self.routes[path]
            request = {}
            request['method'] = method
            request['data'] = data
            for front in self.fronts:
                front(request)
            code, body = controller(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [body]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/html')])
            return [b'Page not found']

