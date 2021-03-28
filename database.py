#!/usr/bin/env python3

import sqlite3
from sqlite3.dbapi2 import connect

# Connect to db and create cursor
def show_all():
    
    conn = sqlite3.connect('customer.db')
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

# Add a new record to the table
def add_one(first, last, email):
    
    # Connect to db and create cursor
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("""
    --sql
    INSERT into customers VALUES (?,?,?) 
    ;
    """, (first, last, email))

    # Close connection
    conn.close()

# remove one record
def delete_one(id):
    
    # Connect to db and create cursor
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()
    cursor.execute("""
    --sql
    DELETE from customers WHERE rowid = (?) 
    ;
    """, id)
    conn.close()