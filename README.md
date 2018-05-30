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
TABLE ministers (name text, riding text, party text, email text, phone text, image_url text)  

![Screenshot](https://s15.postimg.cc/5os3ubem3/Screenshot_from_2018-05-30_07.46.51.png)
