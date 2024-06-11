import sqlite3

def delete_row(table, id, id_value):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        sql_delete_query = f"""DELETE from {table} where {id} = {id_value}"""
        cursor.execute(sql_delete_query)
        connection.commit()
