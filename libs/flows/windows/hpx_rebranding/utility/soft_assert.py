
class SoftAssert:
    def __init__(self):
        self.failures = []

    def _record_failure(self, condition, message):
        if not condition:
            self.failures.append(message)

    def assert_equal(self, actual, expected, message=None):
        self._record_failure(actual == expected, message or f"Expected {expected}, but got {actual}")

    def assert_true(self, condition, message=None):
        self._record_failure(condition, message or "Assertion failed: condition is not True")

    def assert_false(self, condition, message=None):
        self._record_failure(not condition, message or "Assertion failed: condition is not False")

    def assert_contains(self, container, item, message=None):
        self._record_failure(item in container, message or f"{item} not found in {container}")

    def assert_not_contains(self, container, item, message=None):
        self._record_failure(item not in container, message or f"{item} unexpectedly found in {container}")

    def raise_assertion_errors(self):
        if self.failures:
            error_messages = "\n".join(self.failures)
            raise AssertionError(f"Soft assert failures:\n{error_messages}")
