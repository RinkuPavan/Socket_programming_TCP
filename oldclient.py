import socket
import random
# data_payload = 2048
port = 9879
FORMAT = 'utf-8'
DISCONNECT_request = "Disconnect"

#server Which we are connecting
SERVER = socket.gethostbyname(socket.gethostname()) #"192.168.56.1" #for you it should be #'127.0.0.1'
ADDR = (SERVER, port)

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Client.connect(ADDR)

#This function is for sending and receiving data from server.
def send_buy(msg, noOfBooks=1, address_user = None):
    #Due to avoid error of waiting response from server i write here condition. If it will called that time only it will going to ask for data to server and using that we can avoid errors.
    if msg == "Get_OuTPut_From_Server":
        #receiving data from server.
        res_ser = Client.recv(2048).decode(FORMAT)
        #checking data is empty or not
        if res_ser:
            check_book_ = res_ser.split(", ") #spliting the data and checking for user allowed to buy more than 8 books or not.
            #running a loop to iterate whole list
            for i in check_book_:
                #checking if user wllowd to buy books or not.
                if(i == "You are not allowed to Buy more than 8 Number of books... "):
                    print()
                    print(i)
                    return
            #spliting data and restoring it.        
            res_ser = res_ser.split('\n')
            # print(res_ser)
            #Checking list length to filer data.
            len_res_ser = len(res_ser)
            # print(len_res_ser)
            # if(len_res_ser>1):
            #filtering required data
            if len_res_ser == 3:
                print()
                print(res_ser[len_res_ser-2]) #printing the output
                print()
            else:
                print()
                print(res_ser[len_res_ser-3],res_ser[len_res_ser-2]) #printing the output
                print()
            
        #We have user address or not checking that.
        if(address_user == "Get Address From user"):
            #creating a random ordernumber
            order_number = random.randint(1, 1000000)
            #printing required output
            print(f"Thanks for ordering.\nYour Order id is {order_number}. \nWe will Deliver these Books to your Respective Address...\n")
    #when we send message then we need to encode it in byte formate. it's encode string in bytes like object
    message = msg.encode(FORMAT)
    Client.send(message)
    print()
    # print(Client.recv(2048).decode(FORMAT))


def send(msg, noOfBooks=1, address_user = None):
    #Due to avoid error of waiting response from server i write here condition. If it will called that time only it will going to ask for data to server and using that we can avoid errors.
    if msg == "Get_OuTPut_From_Server":
        #In socket programming server will transer all data in maximum two times. so if we are passing data less or equal 2 then there is no issue But when we transfer more than 2 times it can stuck or raise error. So i write here condition using that all those errors will be avoided.
        
        if(noOfBooks<=2):
            for i in range(0,noOfBooks):
                res_ser = Client.recv(2048).decode(FORMAT)
                if res_ser :
                    #checking book is available or not. and take actions according that.
                    if(res_ser == "['Book is Not available which you want... ']"):
                        res_ser = res_ser.replace("[","")
                        res_ser = res_ser.replace("]","")
                        res_ser = res_ser.replace("'","")
                        print(res_ser)
                        print()
                    else:
                        try_ans = []
                        for x in res_ser.split(", "):
                            try_ans.append(x)
                        for y in try_ans:
                            y = y.replace("[", "")
                            y = y.replace("]", "")
                            y = y.replace("'", "")
                            y = y.replace(",", "")
                            print(y)
                        print()
                    # print(list(res_ser))
                    # print(res_ser)
                

        else:
            for i in range(0,2):
                res_ser = Client.recv(2048).decode(FORMAT)
                if res_ser :
                    print(res_ser)
                
            
    #when we send message then we need to encode it in byte formate. it's encode string in bytes like object
    message = msg.encode(FORMAT)
    Client.send(message)
    print()
    # print(Client.recv(2048).decode(FORMAT))


#Below logic is for checking which action user want to perform. and also taken the required input.
cond = True
Check_lst_SB = ["Search", "Buy"]
NumberOfBooks = None
while cond:
    Opt_byclient = input("Hey Do you want to search book Or Buy a Book? \n For Searching book write \"Search\" \n For Searching book write \"Buy\" \n ")
    if Opt_byclient in Check_lst_SB:
        if Opt_byclient == Check_lst_SB[1]:
            NumberOfBooks = int(input(f"How many different books do you want to {Opt_byclient} = "))
        else:
            NumberOfBooks = int(input(f"How many books do you want to {Opt_byclient} = "))
        break
    else:
        print("There is some mistake in which you have written. Please write the exact same word... ")


#Making some list to avoid spelling mistakes in Difficult
SpellMis_Search_difi_easy = ["Eay", "Esy", "asy", "Eas", "easy"]
SpellMis_Search_difi_medi = ["Medim", "Medum", "Mdium", "Meium", "medium"]
SpellMis_Search_difi_hard = ["Hrd", "Had", "ard", "hard"]
orignal_Search_spell = ["Easy", "Hard", "Medium"]
orignal_area_spell = ["peakdistrict","lincoinshire", "york", "peakdistrict", "northwales", "warwickshire", "cheshire"]
#Checking user want to search or buy and taking inputs regarding that.       
if Opt_byclient == Check_lst_SB[0]:
    #I am running a loop here for client how much data he/She wants to search as i told it's Dynamic.
    for i in range (0, NumberOfBooks):
        Area =  input("Area Where Want to Walk = ") or "Client not write it."
        Min_length = (input("Minimum Length in Miles = ") or str(0))
        Max_length = (input("Maximum Length in Miles = ") or str(0))
        Level_dificulty = input("Level of Difficult = ")
        send(Opt_byclient)
        Area = Area.lower() #converting area name into lowercase
        #checking if user write correct area name or not.
        if Area in orignal_area_spell:
            send(Area)
        else:
            Area = input("Please write correct area name : ")
            send(Area.lower())
        send(Min_length)
        send(Max_length)
        #Make some condtions to avoid spelling isuue in Difficult. 
        if Level_dificulty in orignal_Search_spell:
            send(Level_dificulty)
        else:
            if Level_dificulty in SpellMis_Search_difi_easy:
                correct_Word = input("Do you mean \'Easy\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Easy")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
                    
            elif Level_dificulty in SpellMis_Search_difi_medi:
                correct_Word = input("Do you mean \'Medium\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Medium")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
            elif Level_dificulty in SpellMis_Search_difi_hard:
                correct_Word = input("Do you mean \'Hard\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Hard")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
    send("Get_OuTPut_From_Server", NumberOfBooks)

#Taking inputs for Buy oeration.
if Opt_byclient == Check_lst_SB[1]:
    Customer_Name = input("Write Your Name : ")
    for i in range (0, NumberOfBooks):
        Book_Number = input("Book Number which you want to buy : ")
        Book_Quanity = input("Book Quantity which you want for above book : ")
        send_buy(Opt_byclient)
        send_buy(Customer_Name)
        send_buy(Book_Number)
        send_buy(Book_Quanity)
    Your_address = input("Please Write your Full Address for Delivery.")
    send_buy("Get_OuTPut_From_Server", NumberOfBooks, "Get Address From user")
    



# print("are you reaching?")
DISCONNECT_request = DISCONNECT_request.encode(FORMAT)
Client.send(DISCONNECT_request)


