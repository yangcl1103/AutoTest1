from selenium.webdriver.common.by import By


class PublicLocators:
    # 公共定位  左上角消息中心
    messageCenter = (By.XPATH, '/html/body/div[1]/section/header/div/div[2]/div/div/div/div/span')
    # 公共定位  消息中心右键后关闭当前页面
    close = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]')