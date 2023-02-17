
# @pytest.fixture，框架提供的能力。将access_web()打上注解，供别人做初始化的调用。
# scope="class"，作用范围，class 类级别 每个测试类只运行一次
import os
import time

import allure
import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

import base.mailsend
import config.conf
from PageObjects.login_cen.login_cen_bs import LoginBS
from config.conf import URl
from base.screen import save_capture

a=0

@pytest.fixture(scope="session")
def access_web():

    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    desired_capabilities["pageLoadStrategy"] = "none"
    # 实例化对象
    driver = webdriver.Chrome(r'C:\Users\奋斗的小菜鸟\AppData\Local\Programs\Python\Python38\chromedriver.exe')

    # # 窗口最大化
    driver.maximize_window()
    #
    global  a
    driver.get(URl)
    # # 等待
    time.sleep(2)
    # if driver is None:
    #     driver = webdriver.Chrome(r'C:\Users\奋斗的小菜鸟\AppData\Local\Programs\Python\Python38\chromedriver.exe')
    #     driver.maximize_window()
    #     driver.get(URl)
    #     time.sleep(5)

    # 返回对象
    yield driver
    # 后置：关闭浏览器
    # base.mailsend.mailsend(config.conf.messagefilepath)
    driver.quit()


@pytest.fixture
def refresh(access_web):
    yield access_web
    # 刷新页面
    access_web.refresh()
    time.sleep(1)


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", 'P0')
    config.addinivalue_line("markers", 'P1')


from selenium.webdriver.remote.webdriver import WebDriver
import pytest


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        #判断用例是否失败或者xfail跳过的测试
        if (report.skipped and xfail) or (report.failed and not xfail):

            for i in item.funcargs:
                if isinstance(item.funcargs[i], WebDriver):

                    save_capture(item.funcargs[i], "异常截图")
                    pass
                pass
            pass
        report.extra = extra
