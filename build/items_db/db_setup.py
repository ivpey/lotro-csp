import sqlite3
import os
from pathlib import Path

from config import DATA_DIR, BUILD_SCRIPTS_ITEMS_DIR

def setup_db(db_filename:str) -> Path:
    """
        Creates a sqlite .db file with the given name from the schema definition in build/schema.sql

        If such .db file already exists, deletes it and recreates it.

        Args:
            db_filename (str): name for the sqlite database file. Has to include .db extension.

        Returns:
            (Path): full path to the database file.
    """
    
    db_file_loc = DATA_DIR / db_filename
    schema_file_loc = BUILD_SCRIPTS_ITEMS_DIR / 'schema.sql'
    
    # destroy existing database
    if os.path.exists(db_file_loc):
        os.remove(db_file_loc)

    # create from schema
    with open(schema_file_loc, 'r', encoding = 'utf-8') as f:
        schema:str = f.read()

    with sqlite3.connect(db_file_loc) as db_conn:
        crsr = db_conn.cursor()
        db_conn.executescript(schema)

    # ensure that the tables actually exist
    if crsr.execute("SELECT name FROM sqlite_master WHERE name='items'").fetchone() is None:
        raise RuntimeError('Initialization failed for table "items".')
    if crsr.execute("SELECT name FROM sqlite_master WHERE name='progressions'").fetchone() is None:
        raise RuntimeError('Initialization failed for table "progressions".')

    return db_file_loc

if __name__ == '__main__':
    setup_db('lotro-csp.db')