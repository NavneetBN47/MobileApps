# HPX UI Validation Test Automation

This project automates the UI validation for HPX applications using Applitools Eyes for visual testing.  

### Execution

**Test Directory:**

Execute all tests from:

`/MobileApps/tests/windows/hpx/ui_validation`


**Navigate to Test Directory:**

Navigate to test suite:

```bash

cd  MobileApps/tests/windows/hpx/ui_validation

```

**Run Specific Suite:**

```bash

python3  -m  pytest  {test  name}.py  -v  --mobile-device [targetdevice].tgt.ftc.rd.hpicorp.net

```

**Run All Suites:**

```bash

python3  -m  pytest  .  -v  --mobile-device [targetdevice].tgt.ftc.rd.hpicorp.net

```


### Test Results

Validate results at:

[Applitools Dashboard](https://hpeyes.applitools.com/)

### Local API Token
When running tests locally, update the API token in `conftest.py` with your personal token. Set it as an environment variable on the host machine, or hardcode it temporarily (remove before committing code).

  

### Retrieving Your API Token
To retrieve your Applitools API token:

1. Navigate to the [Applitools Dashboard](https://hpeyes.applitools.com/).

2. Select the user icon in the top-right corner.

3. Click on "My API Key" to view or copy your personal API token.

## UI Validation with Applitools Eyes

This project includes a custom `@screenshot_test` decorator to streamline UI validation with Applitools Eyes. The decorator automates common setup and teardown tasks for visual testing, making tests easier to write and maintain. Each test can focus on navigating the application to the correct state, while the decorator handles screenshot capture, validation, and error handling.

### How the `@screenshot_test` Decorator Works

The `@screenshot_test` decorator simplifies the visual testing process by:

1.  **Starting an Applitools Eyes Session**:
    
    -   Each test begins by opening a new session in Applitools Eyes, where `test_name` is used to label and organize the test within Applitools.
2.  **Setting Up the Application State**:
    
    -   Each test is responsible for getting the application into the expected state for validation (e.g., navigating to a specific screen). The decorator takes over from there to handle screenshot capture and validation.
3.  **Capturing a Screenshot**:
    
    -   The decorator captures a screenshot once the application is in the desired state. It generates a unique filename based on the test function name, saves the screenshot in a `screenshots` directory, and then passes it to Applitools for validation.
4.  **Validating with Applitools Eyes**:
    
    -   Applitools Eyes compares the captured screenshot to a stored baseline image. Using AI, Applitools detects visual changes in layout, colors, element visibility, and more. If differences are found, they’re flagged in Applitools’ dashboard for review.
    -   The result includes a URL for reviewing differences and approving baselines if changes are intentional.
5.  **Closing the Applitools Session and Cleanup**:
    
    -   After validation, the session is closed, finalizing the results. Optional cleanup removes screenshot files to keep test environments clean.

### Example Test Structure

Here's an example test using the `@screenshot_test` decorator to validate the layout of the "Audio Control" screen:
    
 

    @pytest.mark.applitools
     @screenshot_test({Set Test Name for Eyes}) 
        def test_verify_audio_control_screen_layout(self, eyes):
	        # Restart Application if Applicable 
            # Set Resolution That Will Be Used in The Test
            # Navigate to page to be validated
            # Make changes that you wish to be validated 

### Setting Up Applitools Eyes

Make sure you have Applitools Eyes configured in your test environment:

1.  **Install Applitools SDK**: `pip install eyes-images`
2.  **Initialize Applitools**: An `eyes` instance for Applitools Eyes is provided through a fixture located in the `conftest.py` file. This fixture makes `eyes` available to any test using the `@screenshot_test` decorator, allowing the decorator to handle all visual validation steps automatically.

### Test Writing Expectations

Each test using `@screenshot_test` should:

-   Validate a single screenshot that captures the screen’s expected layout.
-   Focus only on preparing the application state for validation, allowing the decorator to handle capturing and comparing the screenshot.

This setup ensures reliable, consistent, and maintainable UI validation across multiple tests. Visual test results can be reviewed on Applitools’ dashboard, making it easy to detect and manage UI changes.