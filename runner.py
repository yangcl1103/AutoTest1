import os

import pytest

if __name__ == '__main__':
    # pytest.main()

    # pytest.main(['-m','pp1','--lf','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    pytest.main(['--lf','--alluredir', './Outputs/allure-report/results', '--clean-alluredir'])
    os.system(r"allure generate ./Outputs/allure-report/results -o ./Outputs/allure-report/report --clean")