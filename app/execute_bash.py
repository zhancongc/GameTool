import paramiko


class ExecuteBash(object):
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.ssh = self.obtain_ssh()

    def obtain_ssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.hostname, self.port, self.username, self.password)
        return ssh

    def execute(self, bash):
        stdin, stdout, stderr = self.ssh.exec_command(bash)
        result = stdout.read()
        if not result:
            result = stderr.read()
        return result.decode()
