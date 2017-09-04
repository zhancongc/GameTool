import os
from flask import render_template, request, url_for, send_from_directory, current_app
from . import web
from app.secure_filename import secure_filename
from app.trans_properties import TransProperties


def allowed_file(filename, extensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in extensions


@web.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


@web.route('/out/<filename>')
def out_file(filename):
    return send_from_directory(current_app.config['OUT_FOLDER'], filename)


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/websites')
def websites():
    return render_template('websites.html')


@web.route('/activities', methods=['GET'])
def activities():
    return render_template('activities.html')


@web.route('/activities/start', methods=['POST'])
def start_activities():
    return render_template('output.html')


@web.route('/translate', methods=['GET', 'POST'])
def translate():
    return render_template('translate.html')


@web.route('/translate/sdata', methods=['POST'])
def translate_sdata():
    return render_template('output.html')


@web.route('/translate/properties', methods=['POST'])
def translate_properties():
    properties, excel = request.files['properties'], request.files['excel']
    if properties and excel:
        if allowed_file(properties.filename, ['properties']) and allowed_file(excel.filename, ['xls', 'xlsx']):
            properties_filename, excel_filename = secure_filename(excel.filename), secure_filename(properties.filename)
            properties_path = os.path.join(current_app.config['UPLOAD_FOLDER'], properties_filename)
            excel_path = os.path.join(current_app.config['UPLOAD_FOLDER'], excel_filename)
            properties.save(properties_path)
            excel.save(excel_path)
            example = TransProperties(properties_path, excel_path)
            example.transfer()
            url, warning = url_for('web.out_file', filename='output.properties'), ''
        else:
            url, warning = '', 'File is not allowed due to the unacceptable extension.'
    else:
        url, warning = '', 'File is not found.'
    return render_template('output.html', url=url, warning=warning)


@web.route('/execute', methods=['GET', 'POST'])
def execute():
    return render_template('execute.html')


@web.route('/execute/sql', methods=['GET', 'POST'])
def execute_sql():
    return render_template('output.html')
