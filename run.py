from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['properties', 'xls', 'xlsx'])


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/websites')
def websites():
    return render_template('websites.html')


@app.route('/activities', methods=['GET'])
def activities():
    return render_template('activities.html')


@app.route('/activities/start', methods=['POST'])
def start_activities():
    return render_template('output.html')


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    return render_template('translate.html')


@app.route('/translate/sdata', methods=['POST'])
def translate_sdata():
    return render_template('output.html')


@app.route('/translate/properties', methods=['POST'])
def translate_properties():
    file = request.file['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('output.html', url=url)


@app.route('/execute', methods=['GET', 'POST'])
def execute():
    return render_template('execute.html')


@app.route('/execute/sql', methods=['GET', 'POST'])
def execute_sql():
    return render_template('output.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=65534)
