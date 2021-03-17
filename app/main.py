import uuid
import os
import pprint
from flask import Flask, request, session, render_template, Response

from about.about import about

app = Flask(__name__)
app.debug = True
app.register_blueprint(about, url_prefix='/about')

redis_host = os.getenv('REDIS_SERVER', 'redis')
app.config['SECRET_KEY'] = os.getenv('REDIS_SERVER', 'SetThisAsEnv')

# from lib.lib import getOrder, setOrder

products = [
    { "img" : "gpjb-cr.png", "name" : "Gold Plated Zirconia Ball 1.6"},
    { "img" : "13512.jpg", "name" : "Barbell with 4mm Shamballa Balls"},
    { "img" : "15470.jpg", "name" : "Crazy Lenses with Dracula desing (14mm)"},
    { "img" : "10431.jpg", "name" : "Nipple Shield with Zirconia Chain"}
]


@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route("/test")
def test():
    str = pprint.pformat(request.environ, depth=5)
    return Response(str, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)