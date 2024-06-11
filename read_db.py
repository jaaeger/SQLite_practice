import sqlite3

def read_table(table):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        sqlite_select_query = f"""SELECT * FROM {table}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print(row)
        connection.commit()
