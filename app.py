from flask import Flask, render_template
import os as _os

_sk = _os.path.join(_os.path.dirname(__file__), 'sk')
app = Flask(__name__, template_folder=_os.path.join(_sk, 'templates'), static_folder=_os.path.join(_sk, 'static'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
