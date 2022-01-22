from wframework import render


def index_page(request):
    print(request)
    content = render('templates/index.html', object_list=[{'name': '/index/'}, {'name': '/about/'}])
    return '200 OK', bytes(content, 'utf-8')


def about_page(request):
    print(request)
    content = render('templates/about.html', object_list=[{'name': '/index/'}, {'name': '/about/'}])
    return '200 OK', bytes(content, 'utf-8')
