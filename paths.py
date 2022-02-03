from wframework import render
from models import Site
from reusepatterns.decorators import debug

site = Site()


obj_list = [
    {'name': '/index/'},
    {'name': '/about/'},
    {'name': '/contacts/'},
    {'name': '/add_course/'},
    {'name': '/list_course/'},
    {'name': '/clone_course/'},
]


def index_page(request):
    content = render('index.html', object_list=[*obj_list])
    return '200 OK', bytes(content, 'utf-8')

@debug
def create_course(request):
    if request['method'] == 'POST':
        data = request['data']
        if data:
            name = ''.join(data['name'])
            course = site.create_course('offline', name)
            site.courses.append(course)
        content = render('add_course.html', object_list=[*obj_list])
        return '200 OK', bytes(content, 'utf-8')
    else:
        content = render('add_course.html', object_list=[*obj_list])
        return '200 OK', bytes(content, 'utf-8')

@debug
def clone_course(request):
    if request['method'] == 'POST':
        data = request['data']
        name = ''.join(data['name'])
        old_course = site.get_course(name)
        if old_course:
            new_course = old_course.clone()
            new_course.name = f'{name}_copy'
            site.courses.append(new_course)
        content = render('list.html', object_list=[*obj_list], courses=site.list_courses())
        return '200 OK', bytes(content, 'utf-8')
    else:
        content = render('clone.html', object_list=[*obj_list])
        return '200 OK', bytes(content, 'utf-8')

@debug
def list_course(request):
    content = render('list.html', object_list=[*obj_list], courses=site.list_courses())
    return '200 OK', bytes(content, 'utf-8')


def about_page(request):
    content = render('about.html', object_list=[*obj_list])
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
        content = render('contacts.html', object_list=[*obj_list])
        return '200 OK', bytes(content, 'utf-8')
    else:
        print(f"There is a query string: {request['data']}")
        content = render('contacts.html', object_list=[*obj_list])
        return '200 OK', bytes(content, 'utf-8')
