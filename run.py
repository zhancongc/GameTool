import os
from flask import Flask, render_template, request, url_for, send_from_directory
from property import ALLOWED_EXTENSIONS
from app.secure_filename import secure_filename


app = Flask(__name__)
app.config.from_object('config')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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
    properties, excel = request.files['properties'], request.files['excel']
    if properties and excel:
        if allowed_file(properties.filename) and allowed_file(excel.filename):
            properties_filename, excel_filename = secure_filename(excel.filename), secure_filename(properties.filename)
            properties.save(os.path.join(app.config['UPLOAD_FOLDER'], properties_filename))
            excel.save(os.path.join(app.config['UPLOAD_FOLDER'], excel_filename))
            return render_template('output.html', url=url_for('uploaded_file', filename=properties_filename))
        else:
            return render_template('output.html', warning='File is not allowed due to the unacceptable extension.')
    else:
        return render_template('output.html', warning='File is not found.')


@app.route('/execute', methods=['GET', 'POST'])
def execute():
    return render_template('execute.html')


@app.route('/execute/sql', methods=['GET', 'POST'])
def execute_sql():
    return render_template('output.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=65534)
