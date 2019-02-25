import pymysql.cursors


def getConnect():
    connection = pymysql.Connect(
        host="localhost",
        user="root",
        password="adminroot",
        db="vkbots",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
