from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response

import requests
import os
REST_SERVER = os.environ['REST_SERVER']


def show_books(req):
  data = requests.get(REST_SERVER + "/test").json()
  return render_to_response('templates/test_data.html', {'datas': data}, request=req)


if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('v2', '/')
  config.add_view(show_books, route_name='v2')

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 7070, app)
  server.serve_forever()
