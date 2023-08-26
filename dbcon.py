import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Pavan",
    database="searchtable",
)

mycursor = db.cursor()

# I used below two line code to create database and create table.
# mycursor.execute("CREATE DATABASE SearchTable")
# mycursor.execute("CREATE TABLE Search (Id int PRIMARY KEY AUTO_INCREMENT, Area VARCHAR(50), Book VARCHAR(100), WalkName VARCHAR(100), Distance DOUBLE, Difficult VARCHAR(50), Page int UNSIGNED)")
# mycursor.execute("UPDATE Search SET Area=peakdistrict WHERE Area= PeakDistrict")

"""
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("peakdistrict", "More Peak District", "Hathasage", 7, "Easy", 67))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("peakdistrict", "More Peak District", "Hope and Win Hill", 4.5, "Medium", 18))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("lincoinshire", "Lincolnshire Worlds", "Thornton Abbey", 3.5, "Easy", 20))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("lincoinshire", "Lincolnshire Worlds", "Tennyson County", 5, "Hard", 28))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("york", "Value of York", "Cowlam and Cotham", 8, "Hard", 64))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("york", "Value of York", "Friedaythorpe", 7, "Easy", 42))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("peakdistrict", "Peak District", "Magpie Mine", 4.5, "Medium", 20))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("peakdistrict", "Peak District", "Loard's Seat", 5.5, "Easy", 28))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("northwales", "Snowdonia", "Around Aber", 4, "hard", 24))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("northwales", "Snowdonia", "Yr Eifl", 3.5, "Medium", 42))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("warwickshire", "Malvern and Warwickshire", "Bidford-Upon-Avon", 8.5, "Medium", 78))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("cheshire", "Cheshire", "Dane Valley", 5, "Easy", 20))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("cheshire", "Cheshire", "Malpas", 8.5, "Medium", 80))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("cheshire", "Cheshire", "Farndon", 6, "Hard", 48))
db.commit()
mycursor.execute("INSERT INTO Search (Area, Book, WalkName, Distance, Difficult, Page) VALUES (%s, %s, %s, %s, %s, %s)", ("cheshire", "Cheshire", "Delamere Forest", 5.5, "Easy", 30))
db.commit()
"""


# mycursor.execute("SELECT BOOK, WalkName, page FROM Search where Area ='PeakDistrict'")
# mycursor.execute("DELETE FROM Search WHERE")
# db.commit()
# mycursor.execute("ALTER TABLE Search MODIFY Distance DOUBLE")
# db.commit()
# chek = mycursor.execute("SELECT * FROM search WHERE Area= 'PeakDistrict'")
# print(chek)
# mycursor.execute("SELECT * FROM Search")
# for x in mycursor:
#     print(x)


# print("\n\n")
# if mycursor!= None:

#     print("it's Working")

# else:
#     print("Not Working ")
# for x in mycursor:
#     print(x[0])
#     print(x[1])
#     print(x[2])
# mycursor.execute("SELECT * FROM search")
# for x in mycursor:
#     print(x)
# def test_run(self):
#     mycursor.execute("SELECT * FROM search")

#     for x in mycursor:
#         print(x)
#Add elements to the table



""" BUY TABLE CREATION ADN QUERRY"""
#initial time 
#you have to create table the below line is for create table.
# mycursor.execute("CREATE TABLE Buy (Books VARCHAR(50), Book_Number int UNSIGNED, Price DOUBLE, Book_Quantity int UNSIGNED)")
#adding data to the table
"""
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("More Peak District", 101, 12.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Lincoinshire Worlds", 102, 10.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Value Of York", 103, 11.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Peak District", 104, 12.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Snowdonia", 105, 13.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Malvern and Warwickshire", 106, 10.99, 10))
db.commit()
mycursor.execute("INSERT INTO Buy (Books, Book_Number, Price, Book_Quantity) VALUES (%s, %s, %s, %s)", ("Cheshire", 107, 12.99, 10))
db.commit()
"""
# mycursor.execute("CREATE TABLE Users (UserName VARCHAR(50), portofuser int UNSIGNED, books_buy int UNSIGNED, Total_Cost int UNSIGNED, Back_order int UNSIGNED, Totalprice int UNSIGNED)")
# mycursor.execute("INSERT INTO Users (UserName, portofuser, books_buy, Total_Cost, Back_order, Totalprice) VALUES (%s, %s, %s, 0, 0, 0)", ("Pavan", 62043, 5))
# db.commit()
# mycursor.execute("SELECT * FROM Users")
# myres = mycursor.fetchall()
# for i in myres:
#     # if(i[0] == "192.168.56.1" and i[1] == 62043) :
#     print(i)


# # adding data to buy table
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 101")
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 103")
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 104")
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 105")
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 106")
# mycursor.execute("UPDATE buy SET Book_Quantity=50 WHERE Book_Number= 107")
# db.commit()
# # # #selecting data
# mycursor.execute("SELECT * FROM Buy")
# # #printing for data
# for x in mycursor:
#     print(x)

