from flask import Flask
from flask import send_file
from flask import request
from PIL import ImageGrab
from StringIO import StringIO
import ctypes
user32 = ctypes.windll.user32  # this is the user32.dll reference

MOUSEEVENTF_LEFTDOWN = 2
MOUSEEVENTF_LEFTUP = 4

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/click')
def click():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
    except:
        return 'error: expecting 2 ints, x and y'

    user32.SetCursorPos(x, y)
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return 'done'

@app.route('/desktop.jpeg')
def desktop():
    screen = ImageGrab.grab()
    buf = StringIO()
    screen.save(buf, 'JPEG', quality=75)
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7080, debug=True)
