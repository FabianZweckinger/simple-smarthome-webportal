import flask
import configparser
from waitress import serve

config = configparser.ConfigParser()
config.read('config.ini')
PORT = config.getint("Server", "Port")

app = flask.Flask(__name__)

print("Starting Smarthome Portal Server")


@app.route('/')
def index():
    return app.send_static_file('index.html')


print('Server initialized')
print('Server running on http://localhost:' + str(PORT))
serve(app, host='0.0.0.0', port=PORT)
