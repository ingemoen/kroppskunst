import uuid
import os
import pprint
from flask import Flask, request, session, render_template, Response

########################
## Import MyLibs
########################
from lib.mySql import mySqlQuery

########################
## Import Modules
########################
from about.about import about

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'SetThisAsEnv')
app.register_blueprint(about, url_prefix='/about')

@app.route('/')
def index():

    products = mySqlQuery('dbo.sp_ProductsGet_v3_00 @guid=76393978, @language=no, @page=0, @level0=1, @level1=1, @level2=185, @qtyin=100')
    return render_template('index.html', products=products)

@app.route("/test")
def test():
    str = pprint.pformat(request.environ, depth=5)
    return Response(str, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)