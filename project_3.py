import string
import random

#making a database
database = string.punctuation + string.ascii_letters + string.whitespace + string.digits

#making a list
database = list(database)

#making a copy of database
shuffled_database = database.copy()

#shuffling the database
random.shuffle(shuffled_database)

#taking input
message = list(input("Enter The Message to be Inputed : "))

#making an empty list for storing encrypted message
encrypted_message = ""

#making a range for getting index
for i in message:

#getting index of the message out of databse
    index_of_message = database.index(i)

#storing the equivalent elements of message from shuffled_database
    encrypted_message += shuffled_database[index_of_message]

print(f" \n The Coded Message : {encrypted_message}\n")
print(f"\nOriginal Message was : {message}\n")



    
