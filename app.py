from flask import render_template, Flask, request, url_for, redirect
from speech_to_sign_simulation import run

app = Flask(__name__)

@app.route('/'  )
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        run()

    return redirect(url_for('index'))
        
