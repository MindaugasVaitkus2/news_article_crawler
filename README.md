# Japanese News Article Crawler
This script is aimed to scrape [Gunosy](https://gunosy.com/) to get article text data.
The scraped data contains:

- Text data of contents
- Title
- Date
- Category

The data is considered to be used as data for training classifier or word embedding model. The data is stored in Postgres database.

## How to use 
Clone this repository
```
git clone https://github.com/asahi417/news_article_crawler
cd news_article_crawler
```

First, you need to create config file **password.json**:

```
{
  "host": hostname,
  "user": username,
  "port": port number,
  "db": database name
}
``` 

Then, start postgres database and run script
```
python exe.py
```