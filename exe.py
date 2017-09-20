import json
from os.path import dirname as drn, abspath as abp
from models import crawler, create_log, connectPSQL, ts
from sqlalchemy.sql import select

if __name__ == '__main__':

    # target_cat = [1, 2, 3, 4, 5, 6, 7, 8]
    target_cat = [1, 2]
    max_page = 5

    _p = drn(abp(__file__))
    logger = create_log(_p+"/models/logger")
    with open(_p+'/user_info.json') as f:
        info = json.load(f)

    db_inst = connectPSQL(info)
    con = db_inst.engine.connect()
    time = []
    try:
        for t in target_cat:
            s = select([ts.article_categories.update_time],
                       ts.article_categories.category_ind == t)
            r = con.execute(s)
            time.append([r_ for r_ in r][0][0])
            db_inst.session.query(ts.article_categories).filter(
                ts.article_categories.category_ind == t).delete()
            db_inst.session.commit()

        crawler(logger, max_page=max_page,
                categories=target_cat, update_time=time,
                engine=db_inst.engine)

        # logger.info("inserting data shaped "+str(df_art.shape))
        # df_art.to_sql(ts.article_contents.__tablename__, db_inst.engine,
        #               if_exists='append', index=False)

    except Exception as err:
        logger.error(err)
