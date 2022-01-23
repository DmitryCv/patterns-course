from jinja2 import Template
from urllib.parse import parse_qs


def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)


def parse_data(env):
    if env.get('REQUEST_METHOD') == 'POST':
        content_length = int(env.get('CONTENT_LENGTH'))
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        data = data.decode(encoding='utf-8')
    else:
        data = env.get('QUERY_STRING')
    return parse_qs(data)
