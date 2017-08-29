from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


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
    url = 'http://127.0.0.1:65534/static/img/avatar-lady.jpg'
    return render_template('output.html', url=url)


@app.route('/execute', methods=['GET', 'POST'])
def execute():
    return render_template('execute.html')


@app.route('/execute/sql', methods=['GET', 'POST'])
def execute_sql():
    return render_template('output.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=65534)
