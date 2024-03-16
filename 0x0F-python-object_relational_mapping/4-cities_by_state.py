#!/usr/bin/python3

import MYSQLdb
import sys

if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.states.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
