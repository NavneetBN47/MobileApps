import time
class TaskUtilities(object):
    
    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def register_task(self, execute_name, task_name):
        """
        Registers a scheduled task definition on a local computer.
        """
        self.ssh.send_command('register-ScheduledTask -Action $(New-ScheduledTaskAction -Execute \"{}\") -TaskName \"{}\"'.format(execute_name, task_name), raise_e=False)

    def start_task(self, task_name):
        """
        Starts one or more instances of a scheduled task.
        """
        self.ssh.send_command('Start-ScheduledTask -TaskName  \"{}\"'.format(task_name), raise_e=False)

    def stop_task(self, task_name):
        """
        Stops all running instances of a task.
        """
        self.ssh.send_command('Stop-ScheduledTask -TaskName \"{}\"'.format(task_name), raise_e=False)

    def unregister_task(self, task_name):
        """
        Unregisters a scheduled task.
        """
        self.ssh.send_command('Unregister-ScheduledTask -TaskName  \"{}\" -Confirm:$false'.format(task_name), raise_e=False)

    def verify_eventlog(self, entry_type, message):
        """
        Gets the events in an event log, or a list of the event logs, on the local computer or remote computers.
        """
        result = self.ssh.send_command("get-eventlog -logname application | where-object {$_.EntryType -eq '" + entry_type + "'} | where-object {$_.Message -like '" + message + "'}")
        out = result["stdout"]
        if out == '':
            return True
        else:
            return False
    
    def get_display_resolution(self):
        result = self.ssh.send_command("Get-DisplayResolution")
        out = result["stdout"]
        width = out[out.find("dmPelsWidth"): out.find("dmPelsHeight")].replace("dmPelsWidth", "").replace(":", "").strip()
        height = out[out.find("dmPelsHeight"): out.find("dmDisplayFlags")].replace("dmPelsHeight", "").replace(":", "").strip()
        return width, height 

    def set_display_resolution(self, width, height):
        self.ssh.send_command("Set-DisplayResolution -Width {} -Height {}".format(width, height))

    def restart_fusion_service(self):
        self.ssh.send_command('powershell taskkill /f /im SysInfoCap.exe', raise_e=False, timeout=10)
        time.sleep(5)
        self.ssh.send_command('powershell taskkill /f /im AppHelperCap.exe', raise_e=False, timeout=10)
        time.sleep(5)
        self.ssh.send_command('powershell taskkill /f /im NetworkCap.exe', raise_e=False, timeout=10)
        time.sleep(5)
        self.ssh.send_command('powershell Start-Service -Name HPSysInfoCap', raise_e=False, timeout=10)
        time.sleep(5)
        self.ssh.send_command('powershell Start-Service -Name HPAppHelperCap', raise_e=False, timeout=10)
        time.sleep(5)
        self.ssh.send_command('powershell Start-Service -Name HPNetworkCap', raise_e=False, timeout=10)
        time.sleep(5)
