from Website.Actions import land_to_website
import pytest
import os

driver = land_to_website().driver_path
report_directory = "C:\\Users\\Admin\\Desktop\\Test Websites\\report"
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_") + ".png"
            destinationFile =os.path.join(report_directory,file_name)
            driver.save_screenshot(destinationFile)
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "My very own title!"