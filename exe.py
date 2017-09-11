from models import crawler, create_log, connectPSQL, ts
from sqlalchemy.sql import select

if __name__ == '__main__':
    target_cat = [1, 4]
    max_page = 1
    logger = create_log("./models/logger")
    db_inst = connectPSQL()
    con = db_inst.engine.connect()
    time = []
    for t in target_cat:
        s = select([ts.article_categories.update_time],
                   ts.article_categories.category_ind == t)
        r = con.execute(s)
        time.append([r_ for r_ in r][0][0])
        db_inst.session.query(ts.article_categories).filter(
            ts.article_categories.category_ind == t).delete()
        db_inst.session.commit()

    df_art, df_time = crawler(logger, max_page=max_page, categories=target_cat,
                              update_time=time)

    logger.info("inserting data shaped "+str(df_art.shape))
    df_art.to_sql(ts.article_contents.__tablename__, db_inst.engine,
                  if_exists='append', index=False)
    logger.info("inserting time shaped "+str(df_time.shape))
    df_time.to_sql(ts.article_categories.__tablename__, db_inst.engine,
                   if_exists='append', index=False)
