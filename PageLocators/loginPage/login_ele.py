from selenium.webdriver.common.by import By

class loginElement:
    '''
    页面元素
    '''
    #首界面的“登录”
    login = (By.XPATH, '/html/body/div/section/div/div/div[2]/ul/li[4]/p')

    #切换账户密码登录
    loginTypeChangeTo=(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[4]/a/span')

    #用户名
    user=(By.NAME, 'userName')
    #输入的用户名数据
    userTxt = 'root'

    #密码
    password=(By.NAME, 'password')
    # 输入的密码数据
    passwordTxt = '123456'

    #最终的登录键
    loginFinal=(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/form/div[3]/button')


