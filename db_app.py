#!/usr/bin/env python3

import database

# add records to database
# database.add_one("Laura","Smith","laura@smith.com")

# stuff = [
#    ('Brenda','Smitherton','brenda@smitherton.com'),
#    ('Joshua','Raintree','josh@raintree.com')
# ]

# add many records to database
# database.add_many(stuff)

# Lookup email adress
database.lookup_email("max@example.com")

# delete one element
# database.delete_one('7')

# show all records
database.show_all()
