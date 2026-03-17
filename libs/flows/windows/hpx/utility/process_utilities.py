
class ProcessUtilities(object):

    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def check_process_running(self, process_name):

        if ".exe" in process_name:
            process_name = process_name.replace(".exe", "")

        result = self.ssh.send_command('powershell Get-Process -Name {} '.format(process_name), raise_e=False)
        if not result:
            return False
        if process_name in result["stdout"]:
            return True
        else:
            return False 

        

    def kill_process(self, process_name):

        if self.check_process_running(process_name):
            result = self.ssh.send_command("powershell TASKKILL /F /IM {} ".format(process_name),  raise_e=False)

            if "has been terminated" in result["stdout"]:
                return True
            else:
                return False 
        else:
            return True