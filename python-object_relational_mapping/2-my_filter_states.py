#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = ("SELECT * FROM states WHERE BINARY name = '{}' "
           "ORDER BY id ASC".format(sys.argv[4]))
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
