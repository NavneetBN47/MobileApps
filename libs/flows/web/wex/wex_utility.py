import logging

class SoftAssert:
    """
    A utility class to handle soft assertions.
    Collects assertion errors and reports them at the end of execution.
    """

    def __init__(self):
        super().__init__()
        self.failures = []
        self.passed = []

    def _record_failure(self, condition, message):
        if not condition:
            self.failures.append(message)
        else:
            self.passed.append(message)

    def assert_equal(self, actual, expected, message=None):
        message = message or ""
        if actual == expected:
            self._record_failure(True, f"{message} expected value is {actual} as expected")
        else:
            # If the assertion fails, log the failure message
            self._record_failure(False, f"{message} expected value {expected}, but got value {actual}")

    def assert_true(self, condition, message=None):
        self._record_failure(condition, (message or "") + " is being displayed")
 
    def assert_false(self, condition, message=None):
        self._record_failure(not condition, (message or "") + " should not be displayed")

    def assert_contains(self, container, item, message=None):
        self._record_failure(item in container, message or f"{item} not found in {container}")

    def assert_not_contains(self, container, item, message=None):
        self._record_failure(item not in container, message or f"{item} unexpectedly found in {container}")

    def raise_assertion_errors(self, message=None):
        if self.failures:           
            # Combine all failure messages
            error_messages = "\n".join(self.failures)            
            
            # Raise an AssertionError with all failure messages
            raise AssertionError(f"{message} is not supporting below:\n{error_messages}")

    def generate_report(self, title="Soft Assert Report", message=None):
        """
        Generates a report of passed and failed assertions and logs it to the console.
        """
        report = [f"{title}"]
        if self.passed:
            report.append(f"\n Passed Assertion: {message} is supporting below:")
            report.extend([f"  - {msg}" for msg in self.passed])
        if self.failures:
            report.append(f"\nFailed Assertions: {message} is not supporting below:")
            report.extend([f"  - {msg}" for msg in self.failures])
       
        # Join the report into a single string
        report_content = "\n".join(report)
       
        # Log the report to the console
        logging.info(f"\n{report_content}")
       
        return report_content
   
    def export_report_to_txt(self, filename="soft_assert_report.txt", title="Soft Assert Report", message=None):
        """
        Exports the report of passed and failed assertions to a .txt file.
        """
        # Generate the report
        report_content = self.generate_report(title, message)
       
        # Write the report to a .txt file
        with open(filename, "w") as file:
            file.write(report_content)
       
        # Log the export action
        logging.info(f"Soft Assert Report exported to file: {filename}")
    
    def clear(self):
        self.failures.clear()
        self.passed.clear()