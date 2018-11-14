# MinisterScrape

This program uses the following modules:
```
BeautifulSoup 4
urllib.request
sqlite3
```
This script was made to practice web scraping and SQL database management.  
The program creates a database with contact info on each Member of the Legislative Assembly (MLA) in Alberta, directly scraped from the MLA directory website using Beautifulsoup4.  
The database has the table "ministers" with the following Schema:  
TABLE ministers (name text, riding text, party text, email text, phone text, image_url text)  

![Screenshot](https://s15.postimg.cc/5os3ubem3/Screenshot_from_2018-05-30_07.46.51.png)
