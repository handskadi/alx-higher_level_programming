#!/usr/bin/python3
"""Lists all states from the database."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = conn.cursor()

    cur.execute("SELECT * FROM states")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
