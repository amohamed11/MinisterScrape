from bs4 import BeautifulSoup
import urllib.request
import sqlite3
import re

def table_create(conn):
    c = conn.cursor()

    try:
        c.execute('''CREATE TABLE ministers
               (name text, riding text, party text, email text, phone text, image_url text)''')
    except:
        c.execute(''' DROP TABLE ministers ''')
        table_create(conn)

def insert_minister(conn, name, riding, party, email, phone, image_url):
    c = conn.cursor()

    query = '''INSERT INTO ministers VALUES(?, ?, ?, ?, ?, ?)''' 
    c.execute(query, [name, riding, party, email, phone, image_url])

def main():
    f = urllib.request.urlopen('http://www.assembly.ab.ca/net/index.aspx?p=mla_report&memPhoto=True&alphaboth=True&alphaindex=True&build=y&caucus=All&conoffice=True&legoffice=True&mememail=True') 
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    #Creating the database
    conn = sqlite3.connect("ministers.db")
    table_create(conn)

    #Extracting the Information from the website
    #And then Inserting into the database the extracted Information
    for entry in soup.find_all("div", class_="entry"):
        office = entry.find("div", class_="office")
        #Extracts the email and phone from the contact information
        for contact in office.contents:
            if "Email:" in str(contact):
                email = contact.get_text()
                email = email[6:]

            if "Phone:" in str(contact):
                phone = contact.get_text()
                phone = phone[6:]
        
        member = entry.find("div", class_="member")
        bio = member.contents
        riding = bio[len(bio)-3]

        try:  #Gets the rest of the info of the minister
            name = entry.find("b").get_text()
            image = entry.find('img')
            image_url = image['src']
            image_url = 'http://www.assembly.ab.ca/' + str(image_url[3:])
            party = str(bio[len(bio)-5])
            party = re.sub('[()]', '', party)
        except:  #If there is an error with finding the name, then the position is vacant
            name = "Vacant"
            email = entry.find_next("a").get_text()
            party = 'None'
            image_url = 'None'

        insert_minister(conn, str(name), str(riding), party, str(email), str(phone), str(image_url))
    
    #Commit all the Inserts and close the database
    conn.commit()
    conn.close()

main()
