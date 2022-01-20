import paths
from app import Application, secret_front, other_front
from waitress import serve


app_object = Application(paths.routes, [secret_front, other_front])
serve(app_object, listen='*:8080')