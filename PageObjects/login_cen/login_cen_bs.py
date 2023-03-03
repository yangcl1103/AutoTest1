
import time

import pytest

import TestCases
import TestCases.conftest
from base.base import BasePage
from PageLocators.loginPage.login_ele import loginElement as l
from config import conf as conf




class LoginBS(BasePage):

    def login(self,user_name ='yangcenliang',pass_word = 123456):
        self.click(l.login, doc='首界面的“登录”')
        self.click(l.loginTypeChangeTo, doc='首界面的“切换登录”')
        self.input_text(l.user, user_name, doc='输入账户')
        self.input_text(l.password, pass_word, doc='输入密码')
        self.click(l.loginFinal,doc='点击最终登录')
        time.sleep(1)









