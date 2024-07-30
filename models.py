import sqlalchemy as db
import sqlalchemy.orm as orm
from main import db_path



class Base(db.DeclarativeBase):
    pass


class BankAccount(db.Base):
    __tablename__ = 'bankAccount'

    id = orm.mapped_column(db.Integer, primary_key = True)
    money = orm.mapped_column(db.Float, nullable = False, default=0)
    username = orm.mapped_column(db.String(50), nullable = False, unique=True)
    
    
    