#!/usr/bin/python3

# Initialize a counter variable
counter = 0

# Retrieve all records from the database

# Iterate through the records
for record in database:
# Increment the counter
    counter += 1
    
# Check if the current record is the third one
    if counter % 3 == 0:
# Increment the ID field by 5
        record['ID'] += 5
        
# Update the record in the database 
        