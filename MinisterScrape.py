from bs4 import BeautifulSoup
import urllib.request
import sqlite3

def table_create(conn):
    c = conn.cursor()

    try:
        c.execute('''CREATE TABLE ministers
               (name text, riding text, email text, phone text)''')
    except:
        pass

def insert_minister(conn, name, riding, email, phone):
    c = conn.cursor()

    query = '''INSERT INTO ministers VALUES(?, ?, ?, ?)''' 
    c.execute(query, [name, riding, email, phone])

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
        for child in office.contents:
            if "Email:" in str(child):
                email = child.get_text()
                email = email[6:]

            if "Phone:" in str(child):
                phone = child.get_text()
                phone = phone[6:]

        try:  #Gets the rest of the info of the minister
            name = entry.find("b").get_text()
            member = entry.find("div", class_="member")
            bio = member.contents
            riding = bio[len(bio)-3]
        except:  #If there is an error with finding the name, then the position is vacant
            name = "Vacant"
            member = entry.find("div", class_="member")
            bio = member.contents
            riding = bio[len(bio)-3]
            email = entry.find_next("a").get_text()

        insert_minister(conn, str(name), str(riding), str(email), str(phone))
    
    #Commit all the Inserts and close the database
    conn.commit()
    conn.close()

main()
