from jinja2 import Template


def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


def index_page(request):
    print(request)
    content = render('index.html', object_list=[{'name': '/index/'}, {'name': '/about/'}])
    return '200 OK', bytes(content, 'utf-8')


def about_page(request):
    print(request)
    content = render('about.html', object_list=[{'name': '/index/'}, {'name': '/about/'}])
    return '200 OK', bytes(content, 'utf-8')


class NotFoundPage:
    def __call__(self, request):
        print(request)
        return '404 Not Found', b'404 page not found'


routes = {
    '/': index_page,
    '/index/': index_page,
    '/about/': about_page
}
