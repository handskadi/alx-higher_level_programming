#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    # Connecting to Database
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    # Selecting Data using cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")

    # Print Data
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
