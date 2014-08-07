from bottle import Bottle
from bottle import template, static_file
import platform
hostname = platform.node()

bottle = Bottle()

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def hello():
    return template('index', hostname=hostname)


@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
        return static_file(filepath, root='assets/')

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'

if hostname == 'wojtalke.local':
    bottle.run(host='localhost', port=8002)
