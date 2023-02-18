import os
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from allure import attachment_type

@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
    opts = Options()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
    elif browser == "firefox":
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
    elif browser == "edge":
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opts)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True, scope="session")
def browser(request):
    return request.config.getoption("--browser")

# allure report
# pytest --browser chrome --alluredir=reports/report
# allre serve reports/report
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     # marker = item.get_closest_marker("ui")
#     # if marker:
#     if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
#         try:
#             allure.attach(item.instance.driver.get_screenshot_as_png(),
#                             name=item.name,
#                             attachment_type=allure.attachment_type.PNG)
#         except Exception as e:
#             print(e)


# html report
# pytest --browser chrome --html=reports/report1.html

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'\
                'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
#
# def pytest_html_report_title(report):
#     report.title = "New project"


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://www.yatra.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = item.name + ".png"
#             destination_file = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destination_file)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"'\
#                 'onclick="window.open(this.src)" align="right"/></div>'%file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra