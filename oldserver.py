import socket 
import threading
# from . import dbcon as db
import mysql.connector
#Connecting to DataBase
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "Pavan",
    database="searchtable",
)
mycursor = db.cursor(buffered=True)
cur_for_check_book  = db.cursor(buffered=True)
port = 9879
FORMAT = 'utf-8'
DISCONNECT_request = "Disconnect"
#The below line code can able to select your computer ipv4 address. we don't need to write ip adress manually.
host = socket.gethostbyname(socket.gethostname())     #"192.168.56.1" #'127.0.0.1'

req_binding = (host, port) #we use it in binding with server in future.

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Bind the socket to the port
sock.bind(req_binding)


#The Below Function is for when client buy book from server
def check_buy(ls_buy_req, user_addr):
    #Making empty list for saving answer in future
    ans_buy = ""
    #Making variable for back_order
    back_order = None
    #Filtering userdata from list to add respective variable.
    CustomerName = ls_buy_req[1]
    BookNum = int(ls_buy_req[2])
    BookQuantity = int(ls_buy_req[3])
    # print(CustomerName, BookNum, BookQuantity)
    Buying_book = BookQuantity
    #Adding username to anser
    ans_buy = ans_buy + CustomerName + ", "
    mycursor.execute("SELECT * FROM buy WHERE Book_Number=%s", (BookNum,))
    #getting data from User table.
    cur_for_check_book.execute("SELECT * FROM Users")
    mycur_book_res = cur_for_check_book.fetchall()
    user_books_indb = 0
    check_getin_db = False
    Spent_money_buy = 0
    back_order = 0
    Current_run_cost = 0
    #searching in database
    for i in mycur_book_res:
        #Cheking if Customer Name is exist in databe or not. if exist then getting required data.
        if(i[0] == CustomerName) :
            user_books_indb = i[2]
            Spent_money_buy = i[3]
            back_order = i[4]
            Current_run_cost = i[5]
            check_getin_db = True
    #checking condition if customer name exist if not then adding that data to Users Table.
    if check_getin_db:
        BookQuantity += user_books_indb
        #Updating data in users table.
        cur_for_check_book.execute("UPDATE Users SET books_buy=%s WHERE UserName= %s", (BookQuantity, CustomerName, ))
        db.commit()
    else:
        # print("Inserting... ")
        #inserting Data to Users table.
        cur_for_check_book.execute("INSERT INTO Users (UserName, portofuser, books_buy, Total_Cost, Back_order, Totalprice) VALUES (%s, %s, %s, %s, %s, %s)",(CustomerName,user_addr[1], BookQuantity, Spent_money_buy, back_order, Current_run_cost,) )
        db.commit()
        # print("Data added to users")

    #As you want i set user cann'y buy more that 8 Books.
    if BookQuantity >8:
        # print("You are in 8")
        ans_buy += "You are not allowed to Buy more than 8 Number of books... "
        
    else:
        #running a loop for all required data.
        for x in mycursor:
            #checking required book quanity is exist in database or not.
            if Buying_book <= x[3]:
                #if users buy some book then how much left in database that's storing in variable.
                Left_books = x[3] - Buying_book
                #Taking single book price from database
                Single_book_price = x[2]
                
                #calculating Total Price
                Total_price = Buying_book*Single_book_price
                Spent_money_buy += Total_price
                #updating database.
                Current_run_cost += Total_price
                cur_for_check_book.execute("UPDATE Users SET Total_Cost=%s WHERE UserName= %s",(Spent_money_buy, CustomerName, ))
                db.commit()
                #Checking the cost and set Discount
                if(Current_run_cost>= 75):
                    # Discount = Spent_money_buy %10
                    if Current_run_cost==0:
                        Total_price = Total_price*0.9
                    else:
                        Total_price = Current_run_cost*0.9
                    ans_buy += "Discount of 10% was applied."
                else:
                    Total_price = Current_run_cost
                #adding total price to answer which will send to client.
                ans_buy += " Total Cost of Books " + str(round(Total_price,2)) +". \n"
                cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(Current_run_cost, CustomerName, ))
                db.commit()
                
            else:
                #Taking Back_order
                back_order += Buying_book - x[3]
                available_books = x[3]
                #Taking single book price from database
                Single_book_price = x[2]
                #calculating Total Price
                #updating total price
                Total_price = Buying_book*Single_book_price
                Current_run_cost += Total_price
                #getting total money spend by user.
                Spent_money_buy += Total_price
                #Updating Total money spend by user to Users table.
                cur_for_check_book.execute("UPDATE Users SET Total_Cost=%s WHERE UserName= %s",(Spent_money_buy, CustomerName, ))
                db.commit()
                #Updating back order of user to Users Table.
                cur_for_check_book.execute("UPDATE Users SET Back_order=%s WHERE UserName= %s",(back_order, CustomerName, ))
                db.commit()
                Left_books = 0
                #Checking the cost and set Discount
                if(Current_run_cost>= 75):
                    # Discount = Spent_money_buy %10
                    #adding discount to last price
                    if Current_run_cost==0:
                        Total_price = Total_price*0.9
                    else:
                        Total_price = Current_run_cost*0.9
                    # Total_price = Spent_money_buy*0.9

                    ans_buy += "Discount of 10% was applied."
                else:
                    Total_price = Current_run_cost
                #Creating Required Answer
                ans_buy += " Total Cost of Books " + str(round(Total_price,2)) +". "
                cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(Current_run_cost, CustomerName, ))
                db.commit()
                
        #Updating database here.
        mycursor.execute("UPDATE buy SET Book_Quantity=%s WHERE Book_Number= %s", (Left_books,BookNum,))
        db.commit()

        #checking if there is anything in back order or not.
        if back_order!=0:
            ans_buy += " Books in back order = "+str(back_order) +". \n"

    return ans_buy


#Function for searching data in database and return require output
def check_Search(ls_search_req):
    # print("Inside serch")
    #Declare Variable to do not write same thing multiple time in future.
    Book_is_not = "Book is Not available which you want... "
    ans_sear = []
    # print("[Start Searching...]")
    #Filtering userdata from list to add respective variable.
    Area = ls_search_req[1] 
    Min_len = float(ls_search_req[2])
    Max_len = float(ls_search_req[3])
    LevelOfDifficulty = ls_search_req[4]
    if Area == "Client not write it.":
        #checking if user werite AREA NAME OR NOT
        ans_sear.clear()
        ans_sear.append("Invalid Area Name Where Want to Walk.")
        return ans_sear
    # print(Area, Min_len, Max_len, LevelOfDifficulty)
    mycursor.execute("SELECT * FROM search WHERE Area= %s", (Area,))
    
    # print("what happended")
    #Get data using Querry now we are filterting that data one-by-one and use it as we require.
    for x in mycursor:
        # print("In loop")
        if(x[4]>= Min_len and x[4]<= Max_len):
            if(x[5] == LevelOfDifficulty):
                ans_sear.clear()  #Before Adding data clearing old data if list have.
                ans_sear.append(x[2])  # Appending data into List
                ans_sear.append(x[3])  # Appending data into List
                ans_sear.append(str(x[6]))  # Appending data into List
                print("[Data Passed to user...]")
                return ans_sear
            else:
                #cheking if anser "Book is Not available which you want... " is already added into ans_sear or not if not added then we are adding it.
                if Book_is_not in ans_sear:
                    continue
                ans_sear.append(Book_is_not) # Appending data into List
        else:
            #cheking if anser "Book is Not available which you want... " is already added into ans_sear or not if not added then we are adding it.
            if Book_is_not in ans_sear:
                    continue
            ans_sear.append(Book_is_not)# Appending data into List
    #returing required answer        
    return ans_sear


#Below function is for handle the connection between the client and server
#conn = connection with client(i like to use conn instead of client),  addr = address  
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    # print(type(addr[0]))
    #Create below boolean variable for run while loop and whenever time comes we can break the loop by changing the below variable value. 
    connected = True
    #I create count variable for counting how much time loops runs.
    count = 0
    #I create the below empty list so when data comes from client we can store it in list. And perform some operation like search and buy book.
    temp_ls = []
    ans_sear = []
    ans_buy = []
    while connected:
        #Receiving data from client.
        msg = conn.recv(2048).decode(FORMAT)
        #we require below if condition because when client connect first time he didn't pass any data so it can raise error To solve that error we require this condition.
        if msg:
            count += 1
            #When we get all details and complete all operations we use below conditon and will disconnect client from server. 
            if msg == "Get_OuTPut_From_Server":
                print("Got Connection closing")
                msg = DISCONNECT_request
            if msg == DISCONNECT_request:
                connected = False
                
            #Appending data into the list.
            temp_ls.append(msg)
            # print(temp_ls)
            #when we will get at count 4 then at that time we have required data to perform operations like search and buy so here we are checking that.
            if count == 4:
                #Here we are comparing the first value and finding which operation user want.
                if temp_ls[0] == "Buy":
                    ans_buy = check_buy(temp_ls, addr)
                    if ans_buy:
                        #running s loop to check if user allowed to procced with buy or not if it's not allowed to procced with buy then we are only passing required answer to client.
                        for x in ans_buy:
                            if x == "You are not allowed to Buy more than 8 Number of books... ":
                                ans_buy.clear()
                                ans_buy.append(x)
                        #sending required data to the client
                        conn.send(str(ans_buy).encode(FORMAT))
                        ans_buy= "" #Clearing a List
                        #we are reseting count here because we perform Buy process.
                        count = 0
                

            #When count is on 5 then we have data for Search also we are cross checking it in below.        
            if count == 5:
                if temp_ls[0] == "Search":
                    ans_sear = check_Search(temp_ls)
                    temp_ls.clear()
                    #checking if anser is empty or not
                    if ans_sear:
                        #checking anser length for perform some operations
                        if(len(ans_sear)>1):
                            #getting required data in required variable from list.
                            Recommanded_book = "The Reccomended Book is : " + ans_sear[0]
                            Walk_name_out = "The Walk name is : "+ ans_sear[1]
                            Pages_book = "The page is : "+ ans_sear[2]
                            ans_sear.clear()
                            ans_sear.append(Recommanded_book)
                            ans_sear.append(Walk_name_out)
                            ans_sear.append(Pages_book)
                            conn.send(str(ans_sear).encode(FORMAT)) #Sending data to client
                            ans_sear.clear()  #Clearing a list

                        # print(ans_sear) #Printing a list on server for some test
                        else:
                            conn.send(str(ans_sear).encode(FORMAT)) #Sending data to client.
                            ans_sear.clear()  #Clearing a list
                        # print("Checking list")
                        # print(ans_sear)
                        count = 0
                        # continue
                    
            # print(f"[{addr}] {temp_ls} ")
            # print(f"[{addr}] {msg} + {count}")
            # conn.send("Msg received".encode(FORMAT))
    CustomerName = temp_ls[1]
    cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(0, CustomerName, ))    #Removing Totol session prices from database. So when user login again it's can get new.
    cur_for_check_book.execute("UPDATE Users SET Back_order=%s WHERE UserName= %s",(0, CustomerName, ))
    db.commit()         #Removing back_order from older database.
    temp_ls.clear() #Clearing list
    print("You are Closing the client...")
    conn.close()
    print("Connection is closed...")
        

def start():
    sock.listen()
    print(f"[LISTENING] Server is listening on {host}\n")
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}\n")


print("[STARTING] server is starting...")
start()


