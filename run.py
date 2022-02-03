from paths import *
from wframework import Application
from waitress import serve


def secret_front(request):
    request['secret'] = 'some secret'


routes = {
    '/': index_page,
    '/index/': index_page,
    '/contacts/': contact_page,
    '/about/': about_page,
    '/add_course/': create_course,
    '/list_course/': list_course,
    '/clone_course/': clone_course,
}

app_object = Application(routes, [secret_front])
serve(app_object, listen='*:8080')
