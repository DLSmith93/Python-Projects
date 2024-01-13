

############################################################
## This script is for manipulating databases with SQLite3 ##
############################################################

"""
1. need to use python 3

2. requires two fields to use auto increment and a field with the 
data type string

3. read from suppplied list of files and determine only text files

4. add those files with the extension to a database

5. the script should print the file names to the terminal
"""

import sqlite3

file_list = ("information.docx", "Hello.txt", "myImage.png", \
             "myMovie.mpg", "world.txt", "data.pdf", "myPhoto.jpg")

def create_fileDB(file_list):
    ## creates a new database
    conn = sqlite3.connect("Challanges/script-challanges/testDB.db")
    curr = conn.cursor()

    if conn:
        print("currently creating the database")
        curr.execute("CREATE TABLE IF NOT EXISTS files(file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    file_name TEXT)")
    
        conn.commit()
    else:
        print("was not able to connect to the database")
    conn.close()
 

    conn = sqlite3.connect("Challanges/script-challanges/testDB.db")
    
    if conn:
        print("currently adding data to the database")
        curr = conn.cursor()
        for i in file_list:
            if i.endswith(".txt"):
                print(i)
                curr.execute("INSERT INTO files(file_name) VALUES (?) ", (i,))
        conn.commit()
    else:
        print("was not able to connects to database")

    conn.close()


    conn = sqlite3.connect("Challanges/script-challanges/testDB.db")

    if conn:
        print("currently displaying a table from the database")
        curr = conn.cursor()
        curr.execute("SELECT file_id, file_name FROM files")
        tempTable = (curr.fetchall())

        for item in tempTable:
            print("File_ID: {} -- File_Name: {} ".format(item[0], item[1]))
    else:
        print("was not able to connect to the database")

def create_personDB():

    connection = sqlite3.Connection("Challanges/script-challanges/people_db.db")
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tbl_people(firstName TEXT, lastName TEXT, age INT)")
    c.execute("INSERT INTO tbl_people VALUES ('Devin', 'Smith', 30)")
    connection.commit()
    connection.close()

               
def multiCommands():

    dogValue = ("Cavalier King Charles Spaniel", "Zuko", 1)
    
    with  sqlite3.Connection("Challanges/script-challanges/db_multi.db") as connection:
        c =connection.cursor()
        c.executescript("""CREATE TABLE IF NOT EXISTS tbl_multi(breed TEXT, name TEXT, age INT); \
                        INSERT INTO tbl_multi VALUES ('Cavalier King Charles Spaniel', 'Moka', '2')""")


if __name__ == "__main__":

    choice = 0
    
    while int(choice) != 4:
        print("What action do you want to perform")
        print("1: Create file database")
        print("2: Create people database")
        print("3: execute muptiple sqlite3 commands")
        print("4: Quit")
        choice = input("Please pick an option: ")
        if int(choice) == 1:
            create_fileDB(file_list)
        if int(choice) == 2:
            create_personDB()
        if int(choice) == 3:
            multiCommands()
        if int(choice) == 4:
            quit()

