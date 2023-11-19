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
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
            })

        query_rows = cur.fetchall()

    if query_rows is not None:
        print(", ".join([row[1] for row in query_rows]))
