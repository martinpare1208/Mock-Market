import sqlalchemy as db
import sqlite3
import os
from main import db_path

engine = db.create_engine(f'sqlite:///{db_path}')
print(engine)

async def create_db():
    #Set path for db file
    cwd = os.getcwd()
    db_path = os.path.join(cwd, 'database.db')


    #Create the db file via sqlite3
    conn = sqlite3.connect(db_path)
    