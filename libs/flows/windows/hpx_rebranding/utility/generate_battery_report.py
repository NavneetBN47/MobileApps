import re
import math

def generate_battery_report(self):
    """
    Generates a battery report remotely using powercfg and checks if the output file exists.
    """
    # Define the output file path and the command
    output_file_path = "C:\\Users\\exec\\battery-report.html"
    battery_report_command = f'powercfg /batteryreport /output "{output_file_path}"'
    self.driver.ssh.send_command(f"cmd.exe /c {battery_report_command}")
    return output_file_path

def retrieve_and_parse_battery_report(self, report_path):
    """
    Retrieves the content of the battery report from the remote machine and parses it.
    Fails the test if there are any errors detected.
    """
    # Command to read the content of the report
    read_file_command = f'cmd.exe /c type "{report_path}"'
    file_content = self.driver.ssh.send_command(read_file_command)

    # Ensure file_content is a string
    if isinstance(file_content, dict):
        file_content = file_content.get('stdout', '')

    assert isinstance(file_content, str) and file_content.strip(), "Failed to retrieve valid content from the battery report."

    # Parse the content using regex
    try:
        serial_number_pattern = r"<span class=\"label\">SERIAL NUMBER</span></td><td>(.*?)</td>"
        design_capacity_pattern = r"<span class=\"label\">DESIGN CAPACITY</span></td><td>(.*?) mWh"
        full_charge_capacity_pattern = r"<span class=\"label\">FULL CHARGE CAPACITY</span></td><td>(.*?) mWh"

        serial_number = re.search(serial_number_pattern, file_content, re.DOTALL)
        design_capacity = re.search(design_capacity_pattern, file_content, re.DOTALL)
        full_charge_capacity = re.search(full_charge_capacity_pattern, file_content, re.DOTALL)

        # Convert capacities to integers, rounded down
        def format_capacity(capacity_match):
            if capacity_match:
                capacity_mwh = float(capacity_match.group(1).replace(",", ""))
                return math.floor(capacity_mwh / 1000)  # Convert mWh to WHr and round down
            return None

        # Extract and validate battery info
        battery_info = {
            "SERIAL NUMBER": serial_number.group(1).strip() if serial_number else None,
            "DESIGN CAPACITY": format_capacity(design_capacity),
            "FULL CHARGE CAPACITY": format_capacity(full_charge_capacity),
        }

        # Check for missing or invalid data
        assert None not in battery_info.values(), f"Incomplete or invalid battery report data: {battery_info}"

        return battery_info

    except Exception as e:
        assert False, f"Error parsing battery report content: {e}"
