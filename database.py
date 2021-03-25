#!/usr/bin/env python3

import sqlite3
from sqlite3.dbapi2 import connect


def show_all():

    # Connect to db
    conn = sqlite3.connect('customer.db')

    # Create cursor
    cursor = conn.cursor()

    # Query db
    cursor.execute("""
    --sql
    SELECT rowid, * FROM customers
    ;
    """)
    items = cursor.fetchall()

    for item in items:
        print(item)

    # Commit command
    conn.commit()

    # Close connection
    conn.close()
