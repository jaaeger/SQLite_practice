import sqlite3

from inserts import insert_music_group, insert_person, insert_album, insert_group_person, insert_album_stats

def create_tables():
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        query = """ CREATE TABLE IF NOT EXISTS Music_group(group_id INTEGER PRIMARY KEY, name TEXT NOT NULL)"""
        cursor.execute(query)
        query = """ CREATE TABLE IF NOT EXISTS Person (person_id INTEGER PRIMARY KEY, name TEXT NOT NULL)"""
        cursor.execute(query)
        query = """ CREATE TABLE IF NOT EXISTS Album (album_id INTEGER PRIMARY KEY, name TEXT NOT NULL,
        group_id INTEGER, FOREIGN KEY(group_id) REFERENCES Music_group(group_id))"""
        cursor.execute(query)  # один ко многим (одна группа многим альбомам)
        query = """ CREATE TABLE IF NOT EXISTS Group_person (id INTEGER PRIMARY KEY, group_id INTEGER,
        person_id INTEGER, FOREIGN KEY(group_id) REFERENCES Music_group(group_id), FOREIGN KEY(person_id)
        REFERENCES Person(person_id))"""
        cursor.execute(query)  # многие ко многим (много людей во многих группах)
        query = """ CREATE TABLE IF NOT EXISTS Album_stats (g_id INTEGER PRIMARY KEY, count_albums INTEGER,
        FOREIGN KEY(g_id) REFERENCES Music_group(group_id))"""
        cursor.execute(query)  # один к одному

        connection.commit()


def fill_tables():
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        query = """ INSERT OR REPLACE INTO Music_group(group_id, name) VALUES (?,?); """
        cursor.executemany(query, insert_music_group)
        query = """ INSERT OR REPLACE INTO Person(person_id, name) VALUES (?,?); """
        cursor.executemany(query, insert_person)
        query = """ INSERT OR REPLACE INTO Album(album_id, name, group_id) VALUES (?,?,?); """
        cursor.executemany(query, insert_album)
        query = """ INSERT OR REPLACE INTO Group_person(id, group_id, person_id) VALUES (?,?,?); """
        cursor.executemany(query, insert_group_person)
        query = """ INSERT OR REPLACE INTO Album_stats(g_id, count_albums) VALUES (?,?); """
        cursor.executemany(query, insert_album_stats)

        connection.commit()