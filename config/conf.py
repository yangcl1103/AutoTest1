import os
import time

from selenium.webdriver.common.by import By

# # 项目目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



#测试环境

URl='http://test.yibaiqin.com/home/index/'
# URl='http://beta.yibaiqin.com/home/index/'

#账号密码
##test
USER='yangcenliang'
PASSWORD='123456'
##beta
# user='18782071685@yibaiqin.com'
# password='123456'

#数据库连接地址
##test
host='182.61.131.173'
port='51006'
database='sass'
SQL_USER='root'
SQL_PASSWORD='tahJoh3U'

##beta
#ip=''
#port=''
#SQL_USER='yangcenliang'
#SQL_PASSWORD='123456'


#发送的邮箱账号：
from_addr = 'yangcl1993@126.com'
#发送的邮箱密码：
messagepassword = 'ZWXUMSOKPOVWACRI'  # ZWXUMSOKPOVWACRI

# 收信方邮箱（因为是发送给多个人，所以我们可以用列表进行储存）
to_addrs = ['yangcl1993@126.com', 'yangcenliang@yibaiqin.com']

# 发信服务器
smtp_server = 'smtp.126.com'

#邮件正文
text = time.strftime("%Y-%m-%d", time.localtime(time.time()))+'自动化测试结束，请自行查看报告'

#邮箱端口号,465是端口号，另一个端口号是587
messageport = 465


#邮件附件地址
messagefilepath = r'../Outputs/allure-report/report/index.html'

