import time

import pytest

import TestCases
from TestCases.conftest import refresh
from PageObjects.colleague_cen.colleague_cen_bs import ColleagueBS
from  PageObjects.login_cen.login_cen_bs import  LoginBS
# from TestCases.test_01_login import test_01_login

class TestColleague:

    # 验证同事编辑
    def test_colleague(self, access_web):
        # ColleagueBS(access_web).colleague_select_edit()
        # ColleagueBS(access_web).colleague_add()
        if TestCases.conftest.a ==1:
            pass
        else:
            LoginBS(access_web).login()
        ColleagueBS(access_web).colleague_team()




