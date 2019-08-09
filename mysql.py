import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='47.96.175.196',
                             port= 3307,
                             user='root',
                             password='ahulock2018',
                             db='learning',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #增加信息
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `yss` ( `Fullname`, `age`, `card`, `school`) VALUES (%s, %s,%s, %s)"
    #     cursor.execute(sql, ('maxuedi', '1','P19301132',"安徽大学"))
    # connection.commit()

    #查询信息
    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql ="select `Fullname`,`age`, `card`, `school` from yss WHERE `id`= %s "
    #     cursor.execute(sql,'6')
    #     result = cursor.fetchone()
    #     print(result)

    #更改信息
    # with connection.cursor() as cursor:
    #     sql =' UPDATE yss SET age ="20" WHERE id= %s '
    #     cursor.execute(sql,'6')
    #     connection.commit()
    

    #删除信息
    with connection.cursor() as cursor:
        sql =" DELETE FROM yss WHERE id= %s "
        cursor.execute(sql,'1')
        connection.commit()

finally:
    connection.close()
