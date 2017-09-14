from sqlalchemy import Column, DateTime, Date, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class article_categories(Base):
    __tablename__ = 'article_categories'
    category_ind = Column(Integer, nullable=False, primary_key=True)
    update_time = Column(DateTime, nullable=False)


class article_categories_names(Base):
    __tablename__ = 'article_categories_names'
    category_name = Column(String, nullable=False)
    category_ind = Column(Integer, nullable=False, primary_key=True)


class article_contents(Base):
    __tablename__ = 'article_contents'
    date = Column(DateTime)
    category_ind = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, primary_key=True)
    contents = Column(String, nullable=False)


if __name__ == '__main__':
    s = article_contents()
    print(s.__tablename__)
