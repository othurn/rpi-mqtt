from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import json

BED_ROOM = 'data/bedroom.txt'
LIVING_ROOM = 'data/livingroom.txt'

def open_json(file_path):
  with open(file_path, 'r') as db_file:
    json_obj = json.load(db_file)  
    db_file.close()
  return json_obj

def get_test(req):
  with open('data/test.txt', 'r') as db_file:
    books = json.load(db_file)
  return books

def get_bedroom(req):
  json_data = open_json(BED_ROOM)
  return json_data


def get_living_room(req):
  json_data = open_json(LIVING_ROOM)
  return json_data

def post_bedroom(req):
  # confirm post req
  print('bedroom post accepted')
  text = json.loads(req.body)
  text = json.loads(req.body)
  text = json.loads(req.body)

  print(type(req.body))
  print(text)
  print(type(text))
    
  bedroom = open_json(BED_ROOM)
  print(type(bedroom))
  
  bedroom.append(text)
  bedroom_json = json.dumps(bedroom)
  print(type(bedroom_json))
  f = open('data/bedroom.txt', 'w') 
  f.write(bedroom_json)
  f.close()
  
  # need to return something
  return 'ok'
    
def post_livingroom(req):
  
  print('living room post accepted')
  payload = req.text
  living_room = open_json(LIVING_ROOM)
  living_room.append(payload)
  
  with open('data/livingroom.txt', 'w') as f:
    f.write(json.dumps(living_room))
    f.close()
  
  return 'ok'

if __name__ == '__main__':
  config = Configurator()

  config.add_route('test', '/test')
  config.add_view(get_test, route_name='test', renderer='json')
  
  config.add_route('bedroom', '/bedroom')
  config.add_view(get_bedroom, route_name='bedroom', renderer='json')
  config.add_view(post_bedroom, route_name='bedroom', request_method="POST", renderer='json')
  
  config.add_route('livingroom', '/livingroom')
  config.add_view(get_living_room, route_name='livingroom', renderer='json')
  config.add_view(post_livingroom, route_name='livingroom',    request_method="POST", renderer='json')


  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 7070, app)
  server.serve_forever()
