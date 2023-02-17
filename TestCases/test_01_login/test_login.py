import os
import time

import pytest

import TestCases
from TestCases.conftest import refresh
from  PageObjects.login_cen.login_cen_bs import  LoginBS as  lb

class TestLogin:
    # @pytest.mark.smoke
    # 登录
    # @pytest.mark.parametrize()
    @pytest.mark.run(order=1)
    # @pytest.mark.dependency()
    def test_login(self,access_web):
        TestCases.conftest.a = TestCases.conftest.a + 1
        print(TestCases.conftest.a)
        lb(access_web).login()
        time.sleep(2)
        # assert  1==2











