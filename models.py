import sqlalchemy as db
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base
import os

cwd = os.getcwd()
db_path = os.path.join(cwd, 'database.db')
engine = db.create_engine(f'sqlite:///{db_path}')


Base = declarative_base()

class BankAccount(Base):
    __tablename__ = 'bankAccount'

    id = orm.mapped_column(db.Integer, primary_key = True, autoincrement=True)
    money = orm.mapped_column(db.Float, nullable = False, default=0)
    username = orm.mapped_column(db.String(50), nullable = False, unique=True)
    
    def __init__(self, money, username):
        self.money = money
        self.username = username
        
        
    def __repr__(self):
        return f'{self.id}: {self.username} Total Money: ${self.money}'

#Create the tables
Base.metadata.create_all(engine)
