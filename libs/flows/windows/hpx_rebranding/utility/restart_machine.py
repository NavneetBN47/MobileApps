import time
import subprocess
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.ma_misc import conftest_misc as c_misc
import socket
import requests
import logging


def restart_machine(test_instance, request):
    logging.info("Restarting machine...")
    
    # Get SSH client
    ssh = request.getfixturevalue('ssh_client')
    
    # Get hostname from request config
    hostname = request.config.getoption("--mobile-device")
    
    # Extract port from current driver
    port = _extract_appium_port(test_instance, ssh, hostname)
    
    logging.info(f"Target hostname: {hostname}, Appium port: {port}")
    
    # Close current driver
    try:
        test_instance.fc.driver.quit()
    except:
        pass
    
    # Restart machine
    ssh.send_command('shutdown /r /t 10', raise_e=False)
    
    # Wait for restart (simple ping check)
    logging.info("Waiting for restart...")
    time.sleep(120)  # Wait 2 minutes for shutdown
    
    # Wait for machine back online
    logging.info("Checking if machine is back online...")
    for i in range(60):  # Try for 10 minutes
        try:
            logging.info(f"Ping attempt {i+1}/60...")
            result = subprocess.run(['ping', '-c', '1', hostname], 
                                  capture_output=True, timeout=5)
            if result.returncode == 0:
                logging.info("Machine is back online")
                time.sleep(30)  # Wait for system ready
                break
        except subprocess.TimeoutExpired:
            logging.info(f"Ping timeout on attempt {i+1}")
        except Exception as e:
            logging.info(f"Ping error on attempt {i+1}: {str(e)}")
        time.sleep(10)
    else:
        logging.info("Machine did not come back online within 10 minutes")
        raise Exception("Machine restart timeout")
    
    # Reconnect SSH
    logging.info("Reconnecting SSH...")
    ssh = SSH(hostname, "exec")

    # Wait for Appium server to be ready
    logging.info("Waiting for Appium server to start...")
    if not _wait_for_appium_server(hostname, port=port, timeout=300):
        raise RuntimeError(f"Appium server is not ready on {hostname}:{port} after machine restart")

    # Create new driver
    logging.info("Creating new driver...")
    for i in range(5):  # Try 5 times
        try:
            logging.info(f"Driver creation attempt {i+1}/10...")
            new_driver = c_misc.create_driver(request, "WINDOWS")
            
            # Replace the driver using the correct method
            test_instance.fc.driver.wdvr = new_driver.wdvr
            test_instance.fc.driver.ssh = ssh
            
            logging.info("New driver created and replaced successfully")
            return test_instance.fc.driver
            
        except Exception as e:
            logging.info(f"Driver creation failed on attempt {i+1}: {str(e)}")
            time.sleep(10)
    
    raise Exception("Failed to create new driver")


def _wait_for_appium_server(hostname, port=11000, timeout=300):
    """Wait for Appium server to be ready"""
    logging.info(f"Checking Appium server on {hostname}:{port}")

    start_time = time.time()
    while time.time() - start_time < timeout:
        if _is_port_open(hostname, port):
            logging.info(f"Port {port} is open, checking Appium status...")
            if _check_appium_status(hostname, port):
                logging.info("Appium server is ready")
                return True
        time.sleep(10)

    logging.error(f"Appium server not ready within {timeout} seconds")
    return False


def _is_port_open(hostname, port):
    """Check if a port is open"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            result = sock.connect_ex((hostname, port))
            return result == 0
    except Exception as e:
        logging.warning(f"Socket error: {e}")
        return False


def _check_appium_status(hostname, port):
    """Check if Appium server is responding"""
    try:
        response = requests.get(f"http://{hostname}:{port}/status", timeout=10)
        if response.status_code == 200:
            try:
                status_data = response.json()
                if status_data.get("value", {}).get("ready", True):
                    return True
            except ValueError:
                return True
        return False
    except requests.exceptions.RequestException as e:
        logging.debug(f"Appium status check failed: {e}")
        return False


def _extract_appium_port(test_instance, ssh, hostname):
    """Extract Appium port from driver or detect from remote machine"""
    port = 11000
    
    # Method 1: Extract from driver URL
    try:
        executor_url = test_instance.fc.driver.wdvr.command_executor._url
        logging.info(f"Driver executor URL: {executor_url}")
        import re
        match = re.search(r':(\d+)', executor_url)
        if match:
            port = int(match.group(1))
            logging.info(f"Extracted port from driver URL: {port}")
            return port
        else:
            logging.warning(f"No port pattern found in URL: {executor_url}")
    except Exception as e:
        logging.warning(f"Failed to extract port from driver URL: {e}")
    
    # Method 2: Try to get from capabilities
    try:
        caps = test_instance.fc.driver.wdvr.capabilities
        if 'appium:port' in caps:
            port = int(caps['appium:port'])
            logging.info(f"Extracted port from capabilities: {port}")
            return port
    except Exception as e:
        logging.debug(f"Failed to extract port from capabilities: {e}")
    
    # Method 3: Detect from remote machine
    try:
        logging.info("Attempting to detect Appium port from remote machine...")
        result = ssh.send_command('netstat -ano | findstr "LISTENING" | findstr ":110"', raise_e=False)
        logging.debug(f"Netstat output: {result}")
        
        import re
        for line in result.split('\n'):
            match = re.search(r':(\d{5})\s+.*LISTENING', line)
            if match:
                detected_port = int(match.group(1))
                if 11000 <= detected_port <= 11999:
                    port = detected_port
                    logging.info(f"Detected Appium port from remote machine: {port}")
                    return port
    except Exception as e:
        logging.warning(f"Failed to detect port from remote machine: {e}")
    
    logging.warning(f"Using default port: {port}")
    return port