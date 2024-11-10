import sqlite3

people = [("Jean-Baptiste Zorg", "Human", "122"), ("Korben Dallas", "Meat Popsicle", "100"), ("Ak'not", "Mangalore", "-5")]

with sqlite3.connect(":memory") as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_stuff(name TEXT, species TEXT, IQ INTEGER)")
    cursor.executemany("INSERT INTO tbl_stuff (name, species, IQ) VALUES (?,?,?)", (people))

    cursor.execute("SELECT * FROM tbl_stuff")

    temp = (cursor.fetchall())

    for i in temp:
        print(temp)
