import sqlite3

def update_table(table, set, set_value, id, id_value):
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()
        sql_update_query = f"""Update {table} set {set} = ? where {id} = ?"""
        data = (set_value, id_value)
        cursor.execute(sql_update_query, data)
        connection.commit()
