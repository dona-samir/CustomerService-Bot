import mysql.connector as mysql


conn = mysql.connect(host="localhost", user="root", password="", db="customer service")

cuser =""

def getUser(mail):
    cur = conn.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `email`= '{}'".format(mail)
    cur.execute(qry)
    cuser = cur.fetchone()
    return cuser


def problem(complain,phone):
    cur = conn.cursor(dictionary=True)
    print(cuser)
    qry = "UPDATE `user` set complain = %s , phone = %s where user_id = '{}'".format(cuser['user_id'])
    cur.execute(qry,(complain,phone))
    conn.commit()
    return True 

def getusername():
    return cuser['name']

def save(order_num,deliver,quality,additinalcomplain):
    cur = conn.cursor(dictionary=True)
    qry = "INSERT INTO `Order`  VALUES (%s,%s,%s,%s)"
    cur.execute(qry, (order_num,deliver,quality,additinalcomplain))
    conn.commit()
    return True
