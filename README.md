# MinisterScrape

This program uses the following modules:
```
BeautifulSoup 4
urllib.request
sqlite3
```
I made this to create a database of current ministers of Alberta for a future project of mine.
The program creates a Ministers.db that has a information directly scraped from the MLA directory website.
The database has the table "ministers" with the following Schema:
CREATE TABLE ministers (name text, riding text, email text, phone text)
![Screenshot](https://s7.postimg.cc/6vc8gnxxn/database_example.png)
