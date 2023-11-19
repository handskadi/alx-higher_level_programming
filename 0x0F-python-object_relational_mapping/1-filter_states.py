#!/usr/bin/python3
"""Lists all states from the database Start with N."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Get the statesfrom the database."""
    # Connecting
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    # Defining Cursor & Excute queries
    cur = conn.cursor()
    cur.execute("SELECT * FROM states name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    # Fetch all Queries
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
