import paths


def secret_front(request):
    request['secret'] = 'some secret'


def other_front(request):
    request['key'] = 'value'


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path[-1] != '/':
            path = path + '/'
        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = paths.NotFoundPage()
        request = {}
        for front in self.fronts:
            front(request)
        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body]

