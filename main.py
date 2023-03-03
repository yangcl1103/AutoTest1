import os

import pytest

import base.mailsend

if __name__ == '__main__':
    # pytest.main()

    # 只执行包含login的文件
    # pytest.main(['-s','-k','read','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    # pytest.main(['-vs','login','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    pytest.main(['-vs', '--alluredir', './Outputs/allure-report/results','--self-contained-html','--clean-alluredir'])
    os.system(r"allure generate ./Outputs/allure-report/results -o ./Outputs/allure-report/report --clean")
    # base.mailsend.mailsend()