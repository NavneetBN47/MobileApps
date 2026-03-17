def check_path_exist(ssh, path):
    result = ssh.send_command("Test-Path " + path)
    if "True" in result["stdout"]:
        return True
    else:
        return False