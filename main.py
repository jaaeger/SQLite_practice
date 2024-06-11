import sqlite3

from create_db import create_tables, fill_tables
from read_db import read_table
from update_db import update_table
from delete_db import delete_row

create_tables()
fill_tables()

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # SELECT'ы
    print("Многие ко многим:")
    cursor.execute("""
        SELECT Music_group.name, Person.name 
        FROM Music_group, Person, Group_person
        WHERE (Music_group.group_id = Group_person.group_id AND
               Person.person_id = Group_person.person_id)
        ORDER BY Music_group.name
        """)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print("----------------------------------------------")
    print("Демонстрация LEFT JOIN:")
    cursor.execute("""
        SELECT Album.name, Music_group.name
        FROM Album
        LEFT JOIN Music_group
        ON Album.group_id = Music_group.group_id
        ORDER BY Album.name
    """)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print("----------------------------------------------")
    print("Демонстрация RIGHT JOIN:")
    cursor.execute("""
        SELECT Album.name, Music_group.name
        FROM Album
        RIGHT JOIN Music_group
        ON Album.group_id = Music_group.group_id
        ORDER BY Album.name
    """)
    records = cursor.fetchall()
    for row in records:
        print(row)
    print("----------------------------------------------")
    print("Демонстрация INNER JOIN:")
    cursor.execute("""
        SELECT Album.name, Music_group.name
        FROM Album
        INNER JOIN Music_group
        ON Album.group_id = Music_group.group_id
        ORDER BY Album.name
    """)
    records = cursor.fetchall()
    for row in records:
        print(row)

    connection.commit()

print("----------------------------------------------")
print("Демонстрация read:")
read_table("Album")
print("----------------------------------------------")
print("Демонстрация update:")
update_table("Album", "name", "Aftermathhhhh", "album_id", "7")
read_table("Album")
print("----------------------------------------------")
print("Демонстрация delete:")
delete_row("Album", "album_id", "7")
read_table("Album")