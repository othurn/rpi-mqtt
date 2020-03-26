from wsgiref.simple_server import make_server
from pyramid.config import Configurator
# from pyramid.response import FileResponse

from pyramid.renderers import render_to_response
import json
import os
import requests

def get_home(req):
    
    data = requests.get('http://rest_server:7070/bedroom').json()
    print(data)
    print(type(data))
    return render_to_response('templates/upgraded_home.html', {'data' : data}
                                                               , request=req)

def get_data(req):
    return render_to_response('templates/data.html', {}, request=req)


if __name__ == "__main__":
    with Configurator() as config:
        
        config.include('pyramid_jinja2')
        config.add_jinja2_renderer('.html')
        
        config.add_route('home', '/')
        config.add_view(get_home, route_name = 'home')
        
        config.add_route('data', '/data')
        config.add_view(get_data, route_name='data')
        
        # For CSS
        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        
        app = config.make_wsgi_app()
        
    server = make_server('0.0.0.0', 5050, app)
    server.serve_forever()
