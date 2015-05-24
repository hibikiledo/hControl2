__author__ = 'Hibiki'

from flask import Flask, Response
from flask import render_template

import hstates
import hutils
import hauth


'''
    This is hope to be a clean and stable version of hControl.
    Instead of writing from scratch, hControl2 uses Flask.
'''


# create app instance
app = Flask(__name__)


# setup home state
hstates.add('spotlight-1', hstates.OUTDOOR)


# add index routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# APIs

# handle on, off command from web interface
@app.route('/api/<auth>/<group>/<obj>/<value>', methods=['GET'])
def api_set(auth, group, obj, value):
    if hauth.check(auth):
        return Response(hstates.set(obj, group, value), mimetype='application/json')
    else:
        return Response(hutils.errormsg('Unauthorized Access'), mimetype='application/json')

# handle get command from arduino
@app.route('/api/<auth>/get/<group>/<obj>', methods=['GET'])
def api_get(auth, group, obj):
    if hauth.check(auth):
        return Response(hstates.get(obj, group), mimetype='application/json')
    else:
        return Response(hutils.errormsg('Unauthorized Access'), mimetype='application/json')

# handle report command from web interface & pi
@app.route('/api/<auth>/report', methods=['GET'])
def api_report(auth):
    if hauth.check(auth):
        return Response(hstates.report(), mimetype='application/json')
    else:
        return Response(hutils.errormsg('Unauthorized Access'), mimetype='application/json')

# handle auth request
@app.route('/api/auth/<pub_key>', methods=['GET'])
def api_auth(pub_key):
    return Response(hauth.auth(pub_key), mimetype='application/json')

# run the app
if __name__ == '__main__':
    app.run(debug=True)
