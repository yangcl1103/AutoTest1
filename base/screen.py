import os
import uuid


from selenium.webdriver.remote.webdriver import WebDriver
import allure


def _capture_screenshot(driver: WebDriver):
    fileName =  str(uuid.uuid1()) + '.png'
    driver.get_screenshot_as_file(fileName)
    return fileName


def save_capture(driver: WebDriver, name: str):
    fileName = _capture_screenshot(driver)
    if os.path.exists(fileName):
        allure.attach.file(fileName,
                    attachment_type=allure.attachment_type.PNG, name=name)
        os.remove(fileName)
        pass
    pass
