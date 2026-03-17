
class RegistryUtilities(object):

    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def get_value(self, path, registry_key, expected_value):
        key_value_text = self.ssh.send_command('reg query \"{}\" /v \"{}\"'.format(path, registry_key), raise_e=False)
        if expected_value == key_value_text["stdout"].split("REG_SZ")[1].strip():
            return True
        else:
            return False
    
    def get_value_type_dword(self, path, registry_key, expected_value):
        key_value_text = self.ssh.send_command('reg query \"{}\" /v \"{}\"'.format(path, registry_key), raise_e=False)
        if expected_value == key_value_text["stdout"].split("REG_DWORD")[1][-1].strip():
            return True
        else:
            return False

    def get_registry_value(self, path, registry_key):
        return self.ssh.send_command('reg query \"{}\" /v \"{}\"'.format(path, registry_key), raise_e=False)

    def is_registry_key_name_exist(self, path, registry_key):
        key_name = self.ssh.send_command('reg query \"{}\" /v \"{}\"'.format(path, registry_key), raise_e=False)
        if key_name:
            return True
        else:
            return False  

    def format_registry_path(self, path):
        if "HKEY" in path:
            if "HKEY_CLASSES_ROOT" in path:
                format_path = path.replace("HKEY_CLASSES_ROOT", "HKCR:")
                return format_path
            elif "HKEY_CURRENT_USER" in path:
                format_path = path.replace("HKEY_CURRENT_USER", "HKCU:")
                return format_path
            elif "HKEY_LOCAL_MACHINE" in path:
                format_path = path.replace("HKEY_LOCAL_MACHINE", "HKLM:")
                return format_path
            elif "HKEY_USERS" in path:
                format_path = path.replace("HKEY_USERS", "HKU:")
                return format_path
            elif "HKEY_CURRENT_CONFIG" in path:
                format_path = path.replace("HKEY_CURRENT_CONFIG", "HKCC:")
                return format_path
            else:
                return False
        else:
            return False      

    def add_key(self, path, key_name, key_value,key_type=""):
        if self.is_registry_key_name_exist(path, key_name):
            return True
        else:
            self.ssh.send_command('New-ItemProperty -Path \"{}\" -Name \"{}\" -Value \"{}\"  -PropertyType \"{}\"'.format(self.format_registry_path(path), key_name, key_value, key_type), raise_e=False)
            if self.get_value(path, key_name, key_value):
                return True 
            else:
                return False   

    def update_value(self, path, key_name, key_value):
        if self.is_registry_key_name_exist(path, key_name):
            self.ssh.send_command('Set-Itemproperty -path \"{}\" -Name \"{}\" -Value \"{}\" '.format(self.format_registry_path(path), key_name, key_value), raise_e=False)
            if self.get_value(path, key_name, key_value):
                return True
            else:
                return False
        else:
            return False      
    
    def update_value_type_dword(self, path, key_name, key_value):
        if self.is_registry_key_name_exist(path, key_name):
            self.ssh.send_command('Set-Itemproperty -path \"Registry::{}\" -Name \"{}\" -Value {}'.format(path, key_name, key_value), raise_e=False)
            if self.get_value_type_dword(path, key_name, key_value):
                return True
            else:
                return False
        else:
            return False      

    def delete_key(self, path, key_name):
        if self.is_registry_key_name_exist(path, key_name):
            self.ssh.send_command('Remove-ItemProperty -path \"{}\" -Name \"{}\" '.format(self.format_registry_path(path), key_name), raise_e=False)
            if not self.is_registry_key_name_exist(path, key_name):
                return True
            else:
                return False
        else:
            return False              
   