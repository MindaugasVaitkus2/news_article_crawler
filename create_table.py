import pandas as pd
from models import connectPSQL, ts


def insert_cat(con):
    target = pd.DataFrame(
        [[1, "2016-01-01T00:00:00"],
         [2, "2016-01-01T00:00:00"],
         [3, "2016-01-01T00:00:00"],
         [4, "2016-01-01T00:00:00"],
         [5, "2016-01-01T00:00:00"],
         [6, "2016-01-01T00:00:00"],
         [7, "2016-01-01T00:00:00"],
         [8, "2016-01-01T00:00:00"]],
        columns=["category_ind", "update_time"]
         )
    target.to_sql(ts.article_categories.__tablename__,
                  con.engine, if_exists='replace', index=False)


def insert_catname(con):
    target = pd.DataFrame(
        [[1, "エンタメ"],
         [2, "スポーツ"],
         [3, "おもしろ"],
         [4, "日本"],
         [5, "海外"],
         [6, "コラム"],
         [7, "IT"],
         [8, "グルメ"]],
        columns=["category_ind", "category_name"]
         )
    target.to_sql(ts.article_categories_names.__tablename__,
                  con.engine, if_exists='replace', index=False)


if __name__ == '__main__':
    con = connectPSQL()
    con.create_tables()
    insert_cat(con)
    insert_catname(con)
