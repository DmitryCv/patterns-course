from wframework import render


def index_page(request):
    print(request)
    content = render('templates/index.html', object_list=[{'name': '/index/'},
                                                          {'name': '/about/'},
                                                          {'name': '/contacts/'}])
    return '200 OK', bytes(content, 'utf-8')


def about_page(request):
    print(request)
    content = render('templates/about.html', object_list=[{'name': '/index/'},
                                                          {'name': '/about/'},
                                                          {'name': '/contacts/'}])
    return '200 OK', bytes(content, 'utf-8')


def contact_page(request):
    if request['method'] == 'POST':
        data = request['data']
        title = ''.join(data['title'])
        message = ''.join(data['text'])
        email = ''.join(data['email'])
        print(f"We've got a message: \n"
              f"Title: {title}\n"
              f"Text: {message}\n"
              f"Email: {email}")
        content = render('templates/contacts.html', object_list=[{'name': '/index/'},
                                                             {'name': '/about/'},
                                                             {'name': '/contacts/'}])
        return '200 OK', bytes(content, 'utf-8')
    else:
        print(f"There is a query string: {request['data']}")
        content = render('templates/contacts.html', object_list=[{'name': '/index/'},
                                                                 {'name': '/about/'},
                                                                 {'name': '/contacts/'}])
        return '200 OK', bytes(content, 'utf-8')
