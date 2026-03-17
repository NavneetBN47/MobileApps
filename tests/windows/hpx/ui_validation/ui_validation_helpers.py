import os
import pytest
import tempfile

from applitools.images import Eyes, BatchInfo
import shutil
from functools import wraps
from PIL import Image


def name_screenshot(func, *strings): 
    """
    Generate a screenshot name based on the given function's name and additional strings.

    Args:
        func: The function object whose name will be used.
        strings: Additional strings to append to the function name.

    Returns:
        A string representing the generated screenshot name, ending with .png.

    Raises:
        ValueError: If func is None or does not have a __name__ attribute.
    """
    # Check if func is valid and has a __name__ attribute
    if func is None or not hasattr(func, '__name__'):
        raise ValueError("Invalid function reference provided to name_screenshot")
    
    # Join additional strings with underscores and construct the screenshot name
    additional_text = "_".join(strings)
    screenshot_name = f"{func.__name__}_{additional_text}.png" if additional_text else f"{func.__name__}.png"
    
    return screenshot_name

def screenshot_test(test_name):
    """
    Decorator to set up and tear down visual testing with Applitools, including capturing screenshots.
    
    Args:
        test_name (str): The name for the Applitools test, used for labeling results.
    """
    # The main decorator function that takes the test function as its argument
    def decorator(test_func):
        # Preserve the original function's metadata with wraps
        @wraps(test_func)
        def wrapper(self, eyes, *args, **kwargs):
            """
            Wrapper function to handle visual testing setup, execution, and teardown.
            
            Args:
                self: The test class instance, providing access to class-level attributes.
                eyes: The Applitools Eyes instance, typically initialized via a fixture.
                *args, **kwargs: Additional arguments passed to the test function.
            """
            try:
                # Initialize Applitools Eyes session for visual testing
                eyes.open("myHP UI Validation", test_name)
                
                # Run the actual test function, passing any required arguments
                test_func(self, eyes, *args, **kwargs)
                
                # Generate a unique name for the screenshot based on the test function
                screenshot_name = name_screenshot(test_func)
                
                # Capture a screenshot of the current state of the application and send to eyes
                eyes.check_image(self.driver.wdvr.get_screenshot_as_base64(), screenshot_name)

                # Close the Eyes session and capture the results URL for test reports
                result = eyes.close()
                
                # Assert the test result to ensure it passed validation. If it failed, include the result URL
                assert result, f"Applitools test validation failed. Check test run here: {result.url}"
                
            except ValueError as e:
                pytest.fail(f"An error occurred with input values: {e}", pytrace=True)
            except RuntimeError as e:
                pytest.fail(f"An error occurred during runtime: {e}", pytrace=True)
            except AttributeError as e:
                pytest.fail(f"UI navigation or element interaction failed. Possible missing or undefined attribute: {e}", pytrace=True)
            except FileNotFoundError as e:
                pytest.fail(f"Screenshot file not found for Applitools validation: {e}", pytrace=True)
            except AssertionError as e:
                pytest.fail(f"Applitools validation failed: {e}", pytrace=True)
            except Exception as e:
                pytest.fail(f"An unexpected error occurred: {e}", pytrace=True)
            
            # Return the result of the test function, which is the outcome of the validation
            return result
        return wrapper
    return decorator