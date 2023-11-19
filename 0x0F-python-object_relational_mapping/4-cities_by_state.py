#!/usr/bin/python3
"""Lists all states from the database Start with N."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Get the statesfrom the database."""
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    with conn.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states ON cities.state_id \
                        = states.id ORDER BY cities.id ASC")

        query_rows = cur.fetchall()
    if query_rows is not None:
        for row in query_rows:
            print(row)
