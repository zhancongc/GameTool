import re
import requests
import datetime
from app.parameter import parameters


class Activity(object):
    def __init__(self, ip, country, version, activity_id, parameter, period):
        self.ip = ip
        self.port = self.query()
        self.country = country
        self.version = version
        self.activity_id = activity_id
        self.parameter = self.get_parameter() if not parameter else parameter
        self.period = period
        self.start_time = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S')
        self.end_time = (datetime.datetime.now() +
                         datetime.timedelta(minutes=2) +
                         datetime.timedelta(hours=int(period))
        ).strftime('%Y-%m-%d %H:%M:%S')

    def get_parameter(self):
        if self.activity_id in parameters:
            return parameters[self.activity_id]
        return ''

    def query(self):
        if self.ip == '10.5.201.58':
            path = '/app/foreign_gcld_' + self.version + '_' + self.country + '/backend/apps/'
        elif self.ip == '10.5.201.60':
            path = '/app/nhly_' + self.country + '_' + self.version + '/backend/apps/'
        else:
            return None
        print('path: {0}'.format(path))
        with open(path + 'conf.xml', 'r') as f:
            pattern = re.compile(r'\d{4}')
            arr = pattern.findall(f.read())
            print('socket port: {0}, http port: {1}'.format(arr[0], arr[1]))
        return arr

    def start(self):
        parameter = '''"type":{0},"startTime":"{1}","endTime":"{2}","content":"{3}"'''.format(
            self.activity_id, self.start_time, self.end_time, self.parameter
        )
        parameter = '{' + parameter + '}'
        url = '''http://{0}:{1}/root/gateway.action?command=backstage@activity'''.format(
            self.ip, self.port
        )
        r = requests.post(url, data=parameter)
        return r.text
