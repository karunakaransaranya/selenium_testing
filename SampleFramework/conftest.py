import os
import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action = "store",
        default = "chrome",
        help = "Browser name to run the tests",
    )

@pytest.fixture(scope="function")
def browser_detail(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # ✅ no UI needed in CI
        options.add_argument("--no-sandbox")  # ✅ required in Linux CI
        options.add_argument("--disable-dev-shm-usage")  # ✅ prevents memory issues
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )

            # ✅ Relative path for HTML src attribute
            relative_path = os.path.join("reports", report.nodeid.replace("::", "_") + ".png")
            relative_path = relative_path.replace("\\", "/")  # ✅ fix backslashes for HTML

            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)