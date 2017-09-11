import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

from .db.table_scheme import Base

import logging
import os


def create_log(name):
    """Logging."""
    if os.path.exists(name):
        os.remove(name)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # handler for logger file
    handler1 = logging.FileHandler(name)
    handler1.setFormatter(logging.Formatter(
        "H1, %(asctime)s %(levelname)8s %(message)s"))
    # handler for standard output
    handler2 = logging.StreamHandler()
    handler2.setFormatter(logging.Formatter(
        "H1, %(asctime)s %(levelname)8s %(message)s"))
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    return logger


class connectPSQL:
    def __init__(self):
        info = {
            'host': 'localhost',
            'user': 'Asahi',
            'port': 5432,
            'db': 'c_works'  # postgres
        }

        db = "postgresql+psycopg2://{user}@{host}:{port}/{db}"\
             .format(**info)
        self.engine = create_engine(db)
        session_ = sessionmaker(bind=self.engine)
        self.session = session_()

    def create_tables(self):
        Base.metadata.create_all(self.engine)
        self.session.commit()

    def show_table_name(self):
        sql = """SELECT relname AS table_name FROM pg_stat_user_tables"""
        return pd.read_sql(sql, self.engine)
