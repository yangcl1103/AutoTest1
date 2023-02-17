import config.conf
from base.sqldeal import sqldeal

if __name__ == '__main__':
    sql = "select * from sys_warehouse"
    print(sqldeal(user=config.conf.SQL_USER, password=config.conf.SQL_PASSWORD, sql=sql))