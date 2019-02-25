import connection


def GetUserStats(user_id):
    connect = connection.getConnect()
    try:
        while True:
            with connect.cursor() as cursor:
                sql = f"SELECT * FROM accounts WHERE uid = {user_id}"
                result = cursor.execute(sql)  # Count records
                row = cursor.fetchone()  # Take in the dictionary

                if result >= 1:
                    return row
                else:
                    cursor.execute(f"INSERT INTO accounts(uid, money) VALUES({user_id}, 500)")
                    cursor.execute(f"SELECT * FROM accounts WHERE uid = {user_id}")
                    connect.commit()
                    return row
    finally:
        connect.close()


def addMoney(user_id, money, status):
    connect = connection.getConnect()
    try:
        with connect.cursor() as cursor:
            result = cursor.execute(f"SELECT * FROM `accounts` WHERE `uid` = {user_id}")
            row = cursor.fetchone()
            if status == 1 and result == 1:
                row['money'] += money
            elif status == 2 and result >= 1:
                row['money'] -= money
            cursor.execute(f"UPDATE accounts SET money= {row['money']} WHERE uid = {user_id}")
            connect.commit()
    except:
        connect.close()
