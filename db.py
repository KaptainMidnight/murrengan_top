import mysql.connector


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="adminroot",
        database="vkbots"
    )


def get_user_stats(user_id):
    crs = mydb.cursor(buffered=True)
    sql = "SELECT * FROM `accounts` WHERE `uid` = {user_id}"
    crs.execute(sql)
    row = crs.fetchone()
    print(row)
    try:
        if int(row['uid']) in int(user_id):
            return int(row)
        else:
            sql = "INSERT INTO `accounts`(`uid`, `money`) VALUES ({user_id}, '500')"
            val = [user_id]
            crs.execute(sql, val)
            sql = "SELECT * FROM `accounts` WHERE `uid` = {user_id}"
            crs.execute(sql)
            mydb.commit()
    except:
        print("ERROR")
