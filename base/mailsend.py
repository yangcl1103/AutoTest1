import logging
import os
import smtplib                           #smtplib 用于邮件的发信动作
import time
from email.mime.text import MIMEText         # email 用于构建邮件内容
from email.header import Header                #Header 用来构建邮件头
from email.mime.multipart import MIMEMultipart        #用于实例化附件（处理多种形态的邮件主体我们需要 MIMEMultipart 类）
from loguru import logger

#发信方的信息：发信邮箱，126邮箱授权码
from email.utils import make_msgid

import config.conf


def mailsend(filepath = r'Outputs/allure-report/'):
    from_addr = config.conf.from_addr
    password =config.conf.messagepassword

    #收信方邮箱（因为是发送给多个人，所以我们可以用列表进行储存）
    to_addrs =config.conf.to_addrs

    #发信服务器
    smtp_server = config.conf.smtp_server

    # 创建一个带附件的邮件实例
    message=MIMEMultipart()

    #邮箱正文内容，第一个参数为内容，第二个参数为格式（plain 为纯文本），第三个参数为编码
    text = config.conf.text      #若邮件正文较长，可以这样设置一个变量
    mail_inside = MIMEText(text,'plain','utf-8')             #传入文本，文本类型（plain）、文本编码

    #模拟第三方服务，用smtp发送邮件，总是被当做垃圾邮件退回时：
    message['Message-ID'] = make_msgid()
    #设置邮件头信息
    message['From'] = Header(from_addr)
    message['TO'] = Header(",".join(to_addrs))    #因为是多个邮件，所以需要用join,不信你可以试试不用join看下会报什么错呢
    message['Subject'] = Header(time.strftime("%Y-%m-%d", time.localtime(time.time()))+'自动化测试结果')
    message.attach(mail_inside)                   #传入邮件正文的内容

    #构造附件csv附件1
    #r'../Outputs/allure-report/report/index.html'
    # attr1=MIMEText(open(filepath,'rb').read(),'base64','utf-8')
    # filepathFinal = zip(filepath,'12.bat')
    # print(filepathFinal)
    # attr1=MIMEText(open(filepath,'rb').read(),'base64','utf-8')
    # # attr1=MIMEText(open(r'requirements.txt','rb').read(),'base64','utf-8')
    # attr1["content_Type"]='application/octet-stream'
    # attr1["Content-Disposition"] = 'attachment; filename="index.html"'  # 表示这是附件，名字是啥
    # message.attach(attr1)

    # for filepath_jr in os.listdir(filepath):
    #     attr1=MIMEText(open(os.path.join(filepath, filepath_jr),'rb').read(),'base64','utf-8')
    #     # attr1=MIMEText(open(r'requirements.txt','rb').read(),'base64','utf-8')
    #     attr1["content_Type"]='application/octet-stream'
    #     attr1["Content-Disposition"] = 'attachment; filename="index.html"'  # 表示这是附件，名字是啥
    #     message.attach(attr1)

    # attr2=MIMEText(open(r'12.bat','rb').read(),'base64','utf-8')
    # # attr1=MIMEText(open(r'requirements.txt','rb').read(),'base64','utf-8')
    # attr2["content_Type"]='application/octet-stream'
    # attr2["Content-Disposition"] = 'attachment; filename="index.html"'  # 表示这是附件，名字是啥
    # message.attach(attr2)

    #用于捕捉错误
    try:
        #开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(smtp_server,config.conf.messageport)
        #登录发信邮箱
        server.login(from_addr,password)
        #发送邮件
        server.sendmail(from_addr,to_addrs,message.as_string())
        #关闭服务器
        server.quit()
        logger.info("邮件发送成功")
    except smtplib.SMTPException as e:
        logger.info("邮件发送失败,原因是：{}".format(e))



if __name__ == '__main__':
    mailsend()

