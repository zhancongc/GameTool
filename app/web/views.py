import os
from flask import render_template, request, url_for, send_from_directory, current_app
from . import web
from app.web.forms import ActivitiesForm, ExecuteSQLForm, ExecuteBashForm, PropertiesTranslateForm
from app.secure_filename import secure_filename
from app.trans_properties import TransProperties
from app.start_activity import Activity
from app.execute_bash import ExecuteBash
from app.execute_sql import ExecuteSQL


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


@web.route('/activities/start', methods=['GET', 'POST'])
def start_activities():
    form, result = ActivitiesForm(), ''
    if form.validate_on_submit():
        ip = current_app.config[form.game.data+'_IP']
        activity = Activity(
            ip, form.country.data, form.version.data,
            form.activity_id.data, form.parameter.data, form.period.data
        )
        result = activity.start()
        return render_template('output.html', result=result)
    return render_template('activities.html', form=form)


@web.route('/translate/sdata', methods=['GET', 'POST'])
def translate_sdata():
    return render_template('translate_sdata.html')


@web.route('/translate/properties', methods=['GET', 'POST'])
def translate_properties():
    form, url, result = PropertiesTranslateForm(), '', ''
    if form.validate_on_submit():
        if form.properties and form.excel:
            if allowed_file(form.properties.filename, ['properties']) and allowed_file(form.excel.filename, ['xls', 'xlsx']):
                properties_filename, excel_filename = secure_filename(form.excel.filename), secure_filename(
                    form.properties.filename)
                properties_path = os.path.join(current_app.config['UPLOAD_FOLDER'], properties_filename)
                excel_path = os.path.join(current_app.config['UPLOAD_FOLDER'], excel_filename)
                form.properties.save(properties_path)
                form.excel.save(excel_path)
                example = TransProperties(properties_path, excel_path)
                example.transfer()
                url = url_for('web.out_file', filename='output.properties')
            else:
                result = 'File is not allowed due to the unacceptable extension.'
        else:
            result = 'File is not found.'
        return render_template('output.html', url=url, result=result)
    return render_template('translate_properties.html')


@web.route('/execute/bash', methods=['GET', 'POST'])
def execute_bash():
    form, result = ExecuteBashForm(), ''
    if form.validate_on_submit():
        example = ExecuteBash(form.host.data, int(form.port.data), form.username.data, form.password.data)
        result = example.execute(form.bash.data)
        print(result)
        return render_template('output.html', result=result)
    return render_template('execute_bash.html', form=form)


@web.route('/execute/sql', methods=['GET', 'POST'])
def execute_sql():
    form, result = ExecuteSQLForm(), ''
    if form.validate_on_submit():
        example = ExecuteSQL(form.host.data, int(form.port.data), form.username.data, form.password.data, form.database.data)
        result = example.execute(form.sql.data)
        print(result)
        return render_template('output.html', result=result)
    return render_template('execute_sql.html', form=form)
