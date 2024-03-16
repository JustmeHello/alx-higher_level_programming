#!/usr/bin/python3
""" lists all states from the databse hbtn_0e_0_usa """
import MYSQLdb 
import sys

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE BINARY '{}'"
            .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
