#!/usr/bin/env python3

import database

# add records to database
#database.add_one("Laura","Smith","laura@smith.com")

# delete one element
database.delete_one('7')

# show all records
database.show_all()
