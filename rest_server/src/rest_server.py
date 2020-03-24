from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import json


def get_books(req):
  with open('data/test.txt', 'r') as db_file:
    books = json.load(db_file)
  return books


if __name__ == '__main__':
  config = Configurator()

  config.add_route('rest_route', '/test')
  config.add_view(get_books, route_name='rest_route', renderer='json')

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 7070, app)
  server.serve_forever()
