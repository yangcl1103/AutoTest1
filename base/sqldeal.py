import pymysql
from loguru import logger

import config.conf


def sqldeal(host=config.conf.host, port=config.conf.port,database=config.conf.database
            ,user=config.conf.USER,password=config.conf.PASSWORD,sql=''):
    try:
        db = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                             charset='utf8')
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        logger.info("sql执行成功，sql语句为：{}".format(sql))
    except :
        logger.warning("数据库连接或执行sql语句失败")

    #查询数据
    # lst_data = cursor.fetchall()
    # cursor.close()  # 关闭游标
    # db.close()  # 关闭数据库连接
    # return lst_data
