import time

from selenium.webdriver.common.by import By
from  PageLocators.publicLocators  import  PublicLocators


class colleagueElement(PublicLocators):
    '''
        页面元素
    '''
    # 同事一级菜单
    colleagueFirstLevel = (By.XPATH, '//span[contains(text(),"同事")]')
    # 同事二级菜单
    colleagueSecondLevel = (
    By.XPATH, '//*[@id="app"]/section/section/aside/div/div[1]/div[1]/div/ul/li[2]/ul/li/ul/li[1]')
    # 同事  用户名称输入框
    username = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/div[1]/form/div[1]/div/div/div/input')
    # 同事 查询按钮
    find = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/div[1]/form/div[4]/button[1]/span')
    # 同事_列表 吴千千
    click_wu = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div')
    # 吴千千详情  编辑
    edit = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div[1]/button[1]')
    # 详情的备注
    remark = (By.XPATH,
              '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[19]/div/div/div/input')
    # 详情 保存
    save = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button')
    # 同事 新增按钮
    add = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[1]/button/span')
    # 用户名
    add_username = (By.XPATH,
                    '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input')
    # 微信ID
    add_IDcard = (By.XPATH,
                  '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[2]/div/div[1]/div/input')
    # 婚姻状态
    isMarry = (By.XPATH,
               '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[4]/div/div/div/div/div/input')
    # 未婚
    unMarry = (By.XPATH, '//span[contains(text(),"未婚")]')
    # 手机号码
    phone = (By.XPATH,
             '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[5]/div/div[1]/div/input')
    # 企业微信
    wechatId = (By.XPATH,
                '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/div[2]/div/div[2]/form/div[7]/div/div[1]/div/input')
    # 公司下拉框
    company = (By.XPATH,
               '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div/input')
    # 公司名称
    companyName = (By.XPATH, '//span[contains(text(),"深圳市益佰勤科技有限公司")]')
    # 部门下拉框
    depart = (By.XPATH,
              '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[2]/div[2]/div/form/div[2]/div/div/div/div/div/input')
    # 部门名称
    departName = (By.XPATH, '//span[contains(text(),"IT研发部")]')
    # 工作岗位下拉框
    job = (By.XPATH,
           '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[2]/div[2]/div/form/div[3]/div/div/div/div[2]/div/input')
    # 工作岗位名称
    jobName = (By.XPATH, '//span[contains(text(),"超级管理岗")]')
    # 新增中的保存
    add_save = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/button')
    # svg标签类似于一个图片，定位到他上一级
    # 切换成列表
    stg = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]')
    # 详情
    detail = (By.XPATH,
              '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[9]/div/div/div/button/span')
    # 补充
    buchong = (By.XPATH, '/html/body/div[2]/div[13]/div/div[1]/div/ul/li[2]')
    # qq
    qq = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div/div/div/form/div[1]/div/div/div/input')
    # 补充上的确认
    sure = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[2]/div/div/footer/button[2]/span')

    # ---------------------------------------同事团队----------------------------------------------------------

    # 团队菜单
    team = (By.XPATH, '/html/body/div[1]/section/section/aside/div/div[1]/div[1]/div/ul/li[2]/ul/li/ul/li[3]')
    # 团队详情
    team_detail = (By.XPATH,
                   '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[2]/div/button/span')
    # 详情中的取消
    team_cancel = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div/div/footer/span/button/span')
    # 小三角
    team_svg = (By.XPATH,
                '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/div/i')
    #  详情
    team_sec_detail = (By.XPATH,
                       '/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[2]/td[6]/div/div/div')
    # 团队中的编辑     #/html/body/div[1]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[2]/td[6]/div/div/div/button/span


    team_edit = (By.XPATH, '/html/body/div[2]/div[5]/div/div[1]/div/ul/li')
    team_save = (By.XPATH, '/html/body/div[1]/section/section/main/div/div[2]/div/div/footer/span/button[2]/span')

    team_message_center_rightclick = (By.XPATH, '/html/body/div[1]/section/header/div/div[2]/div/div[1]/div/div/span')
    team_message_center_close = (By.XPATH, '/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]')







