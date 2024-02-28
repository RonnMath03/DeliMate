import pickle as p
import sys
import os
from datetime import date,timedelta

def Main_Menu():
    Menu='\n\
        DeliMate\n\n\
        Main Menu\n\n\
        1: To Add a New Order.\n\
        2: To Search The Recievers Details.\n\
        3: To Display All Existing Orders.\n\
        4: To Modify Order Details.\n\
        5: To Modify Order Status.\n\
        6: To Delete The Order.\n\
        7: To Exit The Program.'
    while True:
        print(Menu)
        ch=int(input('Enter Your Choice: '))
            
        if ch==1:
            while True:
                Add()
                ch1=input("Do you want to Add more orders (Y/N): ")
                if ch1.upper()=="Y":
                    continue
                else:
                    break
            print("_"*150,"\n")
            Main_Menu()       
        elif ch==2:
            Search()
            print("_"*150,"\n")
            Main_Menu()
        elif ch==3:
            Display()
            print("_"*150,"\n")
            Main_Menu()
        elif ch==4:
            Modify_det()
            print("_"*150,"\n")
            Main_Menu()
        elif ch==5:
            Modify_status()
            print("_"*150,"\n")
            Main_Menu()
        elif ch==6:
            Delete()
            print("_"*150,"\n")
            Main_Menu()
        elif ch==7:
            print("You Have Successfully Exited The Program")
            sys.exit()
        else:
            print("Invalid Choice!\nPlease Try Again")
            print("_"*150,"\n")
            Main_Menu()

def Add():
    f=open("dmdb.dat","ab+")
    l=[]
    def Order_no():
        f1=open("dmdb.dat","rb+")
        f2=open("dmdb.dat","ab+")
        order_no=0
        try:
            while True:
                rec=p.load(f1)
                order_no=rec[0]
        except:
            if len(str(order_no))!=4:
                order_no=1000
            else:
                order_no+=1
        l.append(order_no)
        #p.dump(l,f2)
        f1.close()
        f2.close()
    
    Order_no()
    
    def Name():
        nameinput=input("Enter your name: ")
        Name=nameinput.title().strip()
        l.append(Name)
        
    Name()
        
    def Phone_no():
        phone_no= int(input("Enter your Phone Number: +91 "))
        if len(str(phone_no))==10:
            l.append(phone_no)
            
        else:
            print("\n\t\aInvalid Phone Number, Try again!!")
            Phone_no()
            
    Phone_no()
    
    def Address():
        address=input("Enter your address (House name and Town/City): ")
        l.append(address)
        
    Address()
    
    def Pincode():
        pincode=int(input("Enter your Pincode: "))
        if len(str(pincode))==6:
            l.append(pincode)
            
        else:
            print("\n\t\aInvalid Pincode, Try again!!")
            Pincode()
            
    Pincode()
    
    def Order_date():
        
        order_date = str(date.today())
        l.append(order_date)
        
    Order_date()
    
    def Delivery_date():
            order_date = date.today()
            deli_date = order_date + timedelta(days=7)
            l.append(str(deli_date))
            print("\nYour Order will be delivered on",str(deli_date))
            
    Delivery_date()
    
    def Status():
        status="Ordered"
        l.append(status)
        
    Status()
    
    p.dump(l,f)
    f.close()

def Search():
    b="-"*150
    Header='{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'.format\
        ("OrderNo","Name","Phone No.","Address","Pincode","OrderDate",\
         "DeliveryDate","Status")
    def Search_Opt():
        Opt="\n\
        Search using:\n\n\
        1: Order No.\n\
        2: Name\n\
        3: Phone Number\n\
        4: Date of Delivery\n\
        5: Pincode (Area/Locality)\n\
        6: Exit to Main Menu"
        while True:
            print(Opt)
            ch=eval(input("Enter your choice: "))
            if ch==1:
                Search_DB_1()
                print("_"*60,"\n")
                Search_Opt()
            elif ch==2:
                Search_DB_2()
                print("_"*60,"\n")
                Search_Opt()
            elif ch==3:
                Search_DB_3()
                print("_"*60,"\n")
                Search_Opt()
            elif ch==4:
                Search_DB_4()
                print("_"*60,"\n")
                Search_Opt()
            elif ch==5:
                Search_DB_5()
                print("_"*60,"\n")
                Search_Opt()
            elif ch==6:
                print("_"*60,"\n")
                Main_Menu()
            else:
                print("Invalid Choice!!\nTry Again")
                print("_"*60,"\n")
                Search_Opt()
    
    
    def Search_DB_1():
        f1=open("dmdb.dat","rb+")
        orderno=int(input("\nEnter the Order No. to be Searched: "))
    
        try:
            while True:
                rec=p.load(f1)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            print("\nRecord Not Found!!")
        
        f1.close()
        
        print(b)
    
    def Search_DB_2():
        f2=open("dmdb.dat","rb+")
        name_l=input("\nEnter the Name of the customer to be Searched: ")
        name=name_l.title()
        c=0
        try:
            while True:
                rec=p.load(f2)
                if name==rec[1]:
                    c+=1
                    if c==1:
                        print("\nDetails of the Orders of'%s'"%name)
                        print(b)
                        print(Header)
                        print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],\
                                  rec[5],rec[6],rec[7]))
        except:
            if c==0:
                print("\nRecord Not Found!!")
            else:
                print(b)
        f2.close()
        
    def Search_DB_3():
        f3=open("dmdb.dat","rb+")
        Phone=eval(input("\nEnter the Phone No. of the Customer to be Searched: "))
        c=0
        try:
            while True:
                rec=p.load(f3)
                if Phone==rec[2]:
                    c+=1 
                    if c==1:
                        print("\nDetails of the Orders with Phone No:'%s'"%Phone)
                        print(b)
                        print(Header)
                        print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],\
                                  rec[5],rec[6],rec[7]))
        except:
            if c==0:
                print("\nRecord Not Found!!")
            else:
                print(b)
        f3.close()
        
    def Search_DB_4():
        f4=open("dmdb.dat","rb+")
        def Delivery_date():
            try:
                def Day():
                    global dd
                    dds=str(input("Enter the required day of delivery (dd): "))
                    if len(dds)==2:
                        dd=int(dds)
                        
                    else:
                        print("\n\t\aInvalid day, Try again!!")
                        Day()
                        
                Day()
                     
                def Month():
                    global mm
                    mms=str(input("Enter the month of delivery (mm): "))
                    if len(mms)==2:
                        mm=int(mms)
                        
                    else:
                        print("\n\t\aInvalid month, Try again!!")
                        Month()
                        
                Month()
                        
                def Year():
                    global yyyy
                    yyyy=int(input("Enter the year (yyyy): "))
                    if len(str(yyyy))==4 and yyyy>2021:
                        pass
                    
                    else:
                        print("\n\t\aInvalid year, Try again!!")
                        Year()
                        
                Year()
                
                Date= str(date(yyyy,mm,dd))
                return Date
                
            except:
                print("\n\t\aInvalid date, Try again!!")
                Delivery_date()
                    
            
        Date=Delivery_date()
        
        c=0
        try:
            while True:
                rec=p.load(f4)
                if Date==rec[6]:
                    c+=1
                    if c==1:
                        print("\nDetails of the Orders to be delivered on'%s'"%Date)
                        print(b)
                        print(Header)
                        print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],\
                                  rec[5],rec[6],rec[7]))
        except:
            if c==0:
                print("\nRecord Not Found!!\n\
                      Check if the date was entered in the correct format")
            else:
                print(b)
        f4.close()
        
    def Search_DB_5():
        f5=open("dmdb.dat","rb+")
        Pincode=int(input("\nEnter the PINCODE of the area of delivery: "))
        c=0
        try:
            while True:
                rec=p.load(f5)
                if Pincode==rec[4]:
                    c+=1
                    if c==1:
                        print("\nDetails of the Orders\
to be delivered in'%s'"%Pincode)
                        print(b)
                        print(Header)
                        print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],\
                                  rec[5],rec[6],rec[7]))
        except:
            if c==0:
                print("\nRecord Not Found!!")
            else:
                print(b)
        f5.close()
    Search_Opt()

def Display():
    f=open("dmdb.dat","rb+")
    b="="*150
    Header='{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'.format\
        ("OrderNo","Name","Phone No.","Address","Pincode","OrderDate",\
         "DeliveryDate","Status")
    c=0
    try:
        while True:
            c+=1
            rec=p.load(f)
            if c==1:  
                print(b)
                print(Header)
                print(b)
            print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],\
                                  rec[5],rec[6],rec[7]))
    except:
        f.close()
    f.close()
    print(b)     

def Modify_det():
    b="-"*150
    Header='{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'.format\
        ("OrderNo","Name","Phone No.","Address","Pincode","OrderDate",\
         "DeliveryDate","Status")
    orderno=int(input("\nEnter the Order No. to be Modified: "))

    def Find_order():
        f=open("dmdb.dat","rb+")
        try:
            while True:
                rec=p.load(f)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            print("\nRecord Not Found!!")
            f.close()
            Modify_det()
        f.close()
        print(b)
        
    def Display_mod():
        f=open("dmdb.dat","rb+")
        try:
            while True:
                rec=p.load(f)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            f.close()
        f.close()
        print(b)
        
    def Modify_Opt():
        Opt="\n\
        Select the Detail to be Modified:\n\n\
        1: Name\n\
        2: Phone Number\n\
        3: Pincode (Area/Locality)\n\
        4: Address\n\
        5: Exit to Main Menu"
        while True:
            print(Opt)
            ch=eval(input("Enter your choice: "))
            if ch==1:
                Modify_DB_1()
                print("_"*60,"\n")
                Modify_Opt()
            elif ch==2:
                Modify_DB_2()
                print("_"*60,"\n")
                Modify_Opt()
            elif ch==3:
                Modify_DB_3()
                print("_"*60,"\n")
                Modify_Opt()
            elif ch==4:
                Modify_DB_4()
                print("_"*60,"\n")
                Modify_Opt()
            elif ch==5:
                print("_"*60,"\n")
                Main_Menu()
            else:
                print("Invalid Choice!!\nTry Again")
                print("_"*60,"\n")
                Modify_Opt()
                
    def Modify_DB_1():
        f1=open("dmdb.dat","rb+")
        tmp=open("temp.dat","wb+")
        Name_in=input("Enter the new name: ")
        Name=Name_in.title().strip()
        try:
            while True:
                #rpos=f1.tell()
                rec=p.load(f1)
                if rec[0]==orderno:
                    rec[1]=Name
                    #f1.seek(rpos,0)
                    p.dump(rec,tmp)
                    print("\nOrder Successfully Modified!!")
                    continue
                else:
                    p.dump(rec,tmp)     
        except:
            f1.close()
            tmp.close()
        f1.close()
        tmp.close()
        os.remove("dmdb.dat")
        os.rename("temp.dat","dmdb.dat")
        Display_mod()
        print(b)
        
    def Modify_DB_2():
        f2=open("dmdb.dat","rb+")
        tmp=open("temp.dat","wb+")
        def Phone_no():
            phone_no= int(input("Enter the new Phone Number: +91 "))
            if len(str(phone_no))==10:
                Phone=phone_no
                return Phone
            else:
                print("\n\t\aInvalid Phone Number, Try again!!")
                return None      
        Phone=Phone_no()
        while Phone==None:
            Phone=Phone_no()
        try:
            while True:
                #rpos=f2.tell()
                rec=p.load(f2)
                if rec[0]==orderno:
                    rec[2]=Phone
                    #f2.seek(rpos,0)
                    p.dump(rec,tmp)
                    print("\nOrder Successfully Modified!!")
                    continue
                else:
                    p.dump(rec,tmp)     
        except:
            f2.close()
            tmp.close()
        f2.close()
        tmp.close()
        os.remove("dmdb.dat")
        os.rename("temp.dat","dmdb.dat")
        Display_mod()
        print(b)
        
    def Modify_DB_3():
        f3=open("dmdb.dat","rb+")
        tmp=open("temp.dat","wb+")
        def Pin_code():
            pincode=int(input("Enter the new Pincode: "))
            if len(str(pincode))==6:
                Pincode=pincode
                return Pincode
                
            else:
                print("\n\t\aInvalid Pincode, Try again!!")
                return None
            
        Pincode=Pin_code()
        while Pincode==None:
            Pincode=Pin_code()
        try:
            while True:
                #rpos=f3.tell()
                rec=p.load(f3)
                if rec[0]==orderno:
                    rec[4]=Pincode
                    #f3.seek(rpos,0)
                    p.dump(rec,tmp)
                    print("\nOrder Successfully Modified!!")
                    continue
                else:
                    p.dump(rec,tmp)     
        except:
            f3.close()
            tmp.close()
        f3.close()
        tmp.close()
        os.remove("dmdb.dat")
        os.rename("temp.dat","dmdb.dat")
        Display_mod()
        print(b)
        
    def Modify_DB_4():
        f4=open("dmdb.dat","rb+")
        tmp=open("temp.dat","wb+")
        def Address():
            address=input("Enter the new address (House name and Town/City): ")
            return address
        
        Address=Address()
        try:    
            while True:
                #rpos=f4.tell()
                rec=p.load(f4)
                if rec[0]==orderno:
                    rec[3]=Address
                    #f4.seek(rpos,0)
                    p.dump(rec,tmp)
                    print("\nOrder Successfully Modified!!")
                    continue
                else:
                    p.dump(rec,tmp)     
        except:
            f4.close()
            tmp.close()
        f4.close()
        tmp.close()
        os.remove("dmdb.dat")
        os.rename("temp.dat","dmdb.dat")
        Display_mod()
        print(b)
    Find_order()
    Modify_Opt()

def Modify_status():
    b="-"*150
    Header='{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'.format\
        ("OrderNo","Name","Phone No.","Address","Pincode","OrderDate",\
         "DeliveryDate","Status")
    orderno=int(input("\nEnter the Order No. : "))
    def Find_order():
        f=open("dmdb.dat","rb+")
        try:
            while True:
                rec=p.load(f)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            print("\nRecord Not Found!!")
            f.close()
            Modify_status()
        f.close()
        print(b)
        
    def Display_mod():
        f=open("dmdb.dat","rb+")
        try:
            while True:
                rec=p.load(f)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            f.close()
        f.close()
        print(b)
        
    def Status_Opt():
        Opt="\n\
        Choose the Current Status of the Order:\n\n\
        1: Dispatched\n\
        2: In Transit\n\
        3: Out for Delivery\n\
        4: Delivered\n\
        5: Exit to Main Menu"
        while True:
            print(Opt)
            ch=eval(input("Enter your choice: "))
            if ch==1:
                status="Dispatched"
                break
            elif ch==2:
                status="In Transit"
                break
            elif ch==3:
                status="Out for Delivery"
                break
            elif ch==4:
                status="Delivered"
                break
            elif ch==5:
                Main_Menu()
            else:
                Status_Opt()
        f1=open("dmdb.dat","rb+")
        tmp=open("temp.dat","wb+")
        try:
            while True:
                #rpos=f1.tell()
                rec=p.load(f1)
                if rec[0]==orderno:
                    rec[7]=status
                    #f1.seek(rpos,0)
                    p.dump(rec,tmp)
                    print("\nStatus Updated Successfully!!")
                    continue
                else:
                    p.dump(rec,tmp)
        except:
            f1.close()
            tmp.close()
        f1.close()
        tmp.close()
        os.remove("dmdb.dat")
        os.rename("temp.dat","dmdb.dat")
        Display_mod()
    print(b)
    Find_order()
    Status_Opt()

def Delete():
    f=open("dmdb.dat","rb+")
    temp=open("temp.dat","wb+")
    orderno=int(input("\nEnter the order no to be deleted: "))
    b="-"*150
    Header='{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'.format\
        ("OrderNo","Name","Phone No.","Address","Pincode","OrderDate",\
         "DeliveryDate","Status")
   
    def Find_order():
        f1=open("dmdb.dat","rb+")
        try:
            while True:
                rec=p.load(f1)
                if orderno==rec[0]:
                    print("\nDetails of the Order with Order No.'%s'"%orderno)
                    print(b)
                    print(Header)
                    print(b)
                    print('{:<10}{:<16}{:<14}{:<16}{:<12}{:<16}{:<16}{:<16}'\
                          .format(rec[0],rec[1],rec[2],rec[3],rec[4],rec[5],\
                                  rec[6],rec[7]))
                    break
        except:
            print("\nRecord Not Found!!")
            f1.close()
            Delete()
        f1.close()
        print(b)
    
    Find_order()
    
    try:
        while True:
            rec=p.load(f)
            if rec[0]==orderno:
                continue
            else:
                p.dump(rec,temp)
    except:
        f.close()
        temp.close()
        
    f.close()
    temp.close()
    
    os.remove("dmdb.dat")
    os.rename("temp.dat","dmdb.dat")
    print("\nRecord Deleted Sucessfully!!\n")
    Display()
    

Main_Menu()