import os
import time

import pytest

import TestCases
from  TestCases.conftest import refresh
from  PageObjects.login_cen.login_cen_bs import  LoginBS as  lb
from  base.readexcel import read_excel

class TestLogin:
    # @pytest.mark.smoke
    # 登录
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case',read_excel( 'testcase.xlsx','登录','登录'))
    def test_login(self,access_web,case):
        if TestCases.conftest.a == 0:
            TestCases.conftest.a = TestCases.conftest.a + 1
        else:
            pass
        xh,gn,case_name,para,is_exc,exc_result=case
        para_final = eval(para)
        lb(access_web).login(para_final['username'],para_final['password'])
        time.sleep(3)
        # assert  1==2











