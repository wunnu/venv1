from pymysql import Connection


def mysql_conn():
    # 连接数据库用
    conn = Connection(host='localhost', user='root', password='1234abcd', port=3306, database='db1')
    cursor = conn.cursor()
    # 往名为l的表格中插入姓名和对应年龄


    # 插入内容写好后要进行提交

    ttr='ddd'
    #cursor.execute('drop table aa')
    cursor.execute("insert into tb1(name) values ("'"+ttr+"'" )")
    # 数据库事务的提交
    conn.commit()

    # 测试是否提交成功
    print('插入成功！')

    # 提取表中第一个内容
    # print(cursor.fetchone())
    # 如果提取过第一个内容，则是提取前三个
    # print(cursor.fetchmany(3))
    # 如运行过前两个，则显示除提取后剩下的全部
    # print(cursor.fetchall())

    # 结束关闭 cursor  connection
    cursor.close()
    conn.close()






if __name__ == '__main__':

    mysql_conn()
