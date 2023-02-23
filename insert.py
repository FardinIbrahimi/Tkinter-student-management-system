from customtkinter import *

import sqlite3 as sql

from tkinter import ttk

import sqlite3 as sql

from time import sleep


splash_root = CTk()

splash_root.geometry ("300x300")

set_appearance_mode("dark")

set_default_color_theme("blue")

label1 = CTkLabel(master = splash_root, text = "LOADING...")
label1.grid(padx = 70, pady = 10, row = 1)

from PIL import Image, ImageTk
splashlogo = Image.open("smslogo.png")
splashlogo = splashlogo.resize((200,100))
splashlogo = ImageTk.PhotoImage(splashlogo)
splashlogo = CTkLabel(master = splash_root, image = splashlogo, text = None)
splashlogo.grid(padx = 70, pady = 10, row = 2)

label2 = CTkLabel(master = splash_root, text = "School Management System")
label2.grid(padx = 20, pady = 20, row = 3)


def main_window():
    
    splash_root.destroy()
    
    connection = sql.connect("stundents.db")

    cursor = connection.cursor()

    #cursor.execute("create table student (name text, lastname text, age integer, fee integer, mobile text)")

    def insert ():
        
        name = studentname.get()
        
        lastname = studentlastname.get()
        
        age = studentage.get()
        
        fee =  studentfee.get()
        
        mobile = studentmobile.get()
        
        studentname.delete(0, END)
        
        studentlastname.delete(0,END)
        
        studentage.delete(0, END)
        
        studentfee.delete(0, END)
        
        studentmobile.delete(0, END)
        
        ## inserting data to database
        cursor.execute ("insert into student values (?,?,?,?,?)", (name, lastname, age, fee, mobile))
        
        print ("success!")
        
        connection.commit()

    set_appearance_mode("dark")

    set_default_color_theme("blue")

    root = CTk()

    root.geometry ('1300x500')

    root.title ('Student Management System')

    style = ttk.Style(root)

    def update ():
        
        updatescreen = CTkToplevel()
        
        updatescreen.geometry('250x250')
        
        updatescreen.title("update a record")
        
        set_appearance_mode("dark")
        
        set_default_color_theme("blue")
        
        updatelabel = CTkLabel(master = updatescreen, text = "Update the record!").pack(padx = 10, pady = 10)
        
        mobiletoupdate = CTkEntry(master = updatescreen, width = 200)
        
        mobiletoupdate.pack(padx = 10, pady = 10)
        
        def updatepage():
                                    
            updatepage = CTkToplevel()
            updatepage.geometry("500x500")
            updatepage.title("Update")
            
            query4all = cursor.execute(f"select * from student where mobile = {mobiletoupdate.get()}")
            namequery = CTkEntry(master = updatepage, width = 250)
            namequery.pack (padx = 10, pady = 10)
            lastnamequery = CTkEntry(master = updatepage, width = 250)
            lastnamequery.pack (padx = 10, pady = 10)
            agequery = CTkEntry(master = updatepage, width = 250)
            agequery.pack (padx = 10, pady = 10)
            feequery = CTkEntry(master = updatepage, width = 250)
            feequery.pack (padx = 10, pady = 10)
            mobilequery = CTkEntry(master = updatepage, width = 250)
            mobilequery.pack (padx = 10, pady = 10)
            for record in query4all:
                namequery.insert (0, record[0])
                lastnamequery.insert (0, record[1])
                agequery.insert(0, record[2])
                feequery.insert(0,record[3])
                mobilequery.insert(0,record[4])
                
            def finalupdate():
                
                cursor.execute("update student set name = :name, lastname = :lastname, age = :age, fee = :fee, mobile = :mobile where mobile = :mobile", {'name':namequery.get(), 'lastname':lastnamequery.get(), 'age':agequery.get(), 'fee':feequery.get(), 'mobile':mobiletoupdate.get()})
                
                connection.commit()
                
            finalupdatebutton = CTkButton(master = updatepage, text = "Update", command = finalupdate)
            finalupdatebutton.pack(padx = 10, pady = 10)
            
            updatepage.mainloop()
        
        updatebuttonconfirm = CTkButton(master = updatescreen, text = "Update", command = updatepage, width = 200)
        
        updatebuttonconfirm.pack(padx = 10, pady = 20)
        
        updatescreen.mainloop()
        
        
    def deletepage():
        
        deletepage1 = CTkToplevel()
        
        deletepage1.geometry('250x250')
        
        deletepage1.title("Delete any record using mobile number.")
        
        mobile2delete = CTkEntry(master = deletepage1)
        
        mobile2delete.pack(padx = 10, pady = 10)
        
        
        def deletefunction():
            
            cursor.execute("delete from student where mobile = :mobile", {'mobile':mobile2delete.get()})
            
            connection.commit()
        
        deletebutton2 = CTkButton(master = deletepage1, text = "Delete",command = deletefunction)
    
        deletebutton2.pack(padx = 10, pady = 10)
        
        deletepage1.mainloop()
        
    
    
    
    ####LOGO AREA
    from PIL import Image, ImageTk
    Logo = Image.open("smslogo.png")
    Logo = Logo.resize((300,150))
    Logo = ImageTk.PhotoImage(Logo)
    namelabel = CTkLabel(master = root, text = None, image=Logo)
    namelabel.grid(padx = 10, pady = 10, column = 0, row = 0, columnspan = 5)
    
    
    
    
    #### entries
    studentname = CTkEntry(master = root, width = 250, placeholder_text="Name")

    studentname.grid (column = 0, row = 3, padx = 10, pady = 10)

    studentlastname = CTkEntry(master = root, width = 250, placeholder_text="Last Name")

    studentlastname.grid (column = 1, row = 3, padx = 10, pady = 10)

    studentage = CTkEntry(master = root, width = 250, placeholder_text="Age")

    studentage.grid (column = 2, row = 3, padx = 10, pady = 10)

    studentfee = CTkEntry(master = root, width = 250, placeholder_text="Fee")

    studentfee.grid (column = 3, row = 3, padx = 10, pady = 10)

    studentmobile = CTkEntry(master = root, width = 250, placeholder_text="Mobile")

    studentmobile.grid (column = 4, row = 3, padx = 10, pady = 10)

    ##### buttons
    savebutton = CTkButton(master = root, width = 250, text = "Insert", command = insert)

    savebutton.grid (column = 0, row = 4, padx = 10, pady = 10)


    deletebutton = CTkButton(master = root, width = 250, text = "Delete", command = deletepage)

    deletebutton.grid (column = 2, row = 4, padx = 10, pady = 10)

    
    def find ():
        find_root = CTk()
        find_root.geometry("800x100")
        set_appearance_mode("dark")
        
        searchbox = CTkEntry(master = find_root,width = 250, placeholder_text = "Search...")
        searchbox.grid (padx = 10, pady = 10, column = 1, row = 1)
        
        filtersearch = CTkComboBox(master = find_root, values = ("Name","Last name","Age","Mobile"))
        filtersearch.grid (padx = 10,pady = 10, column = 2, row = 1)
        
        def goandfind():
            
            if filtersearch.get() == "Name":
                sql = "select * from student where name = :filter"
                
            elif filtersearch.get() == "Last name":
                sql = "select * from student where lastname = :filter"
                
            elif filtersearch.get() == "Age":
                sql = "select * from student where age = :filter"
                
            elif filtersearch.get() == "Mobile":
                sql = "select * from student where mobile = :filter"
                
                
            
            searched = searchbox.get()
            searchresult = cursor.execute(sql, {'filter':searched})
            searchresult = cursor.fetchall()
            
            
            for searchstaff in searchresult:
                searchresult = CTkButton(master = find_root,text = f"Name: {searchstaff[0]}", width = 200)
                searchresult.grid (padx = 10, pady = 10, column = 1, row = 3)
                
                searchresult = CTkButton(master = find_root,text = f"Last Name: {searchstaff[1]}", width = 50)
                searchresult.grid (padx = 10, pady = 10, column = 2, row = 3)
                
                searchresult = CTkButton(master = find_root,text = f"Age: {searchstaff[2]}", width = 50)
                searchresult.grid (padx = 10, pady = 10, column = 3, row = 3)
                
                searchresult = CTkButton(master = find_root,text = f"Fee: {searchstaff[3]}", width = 50)
                searchresult.grid (padx = 10, pady = 10, column = 4, row = 3)
                
                searchresult = CTkButton(master = find_root,text = f"Mobile: {searchstaff[4]}", width = 50)
                searchresult.grid (padx = 10, pady = 10, column = 5, row = 3)
                
            if not searchresult:
                
                CTkLabel(master = find_root, text = "No such record!", width = 100).grid (padx = 10, pady = 10, column = 1, row = 3, columnspan = 5)
                
            
        searchbutton = CTkButton(master = find_root, text = "SEARCH / GO", command = goandfind, width = 330)
        searchbutton.grid(padx = 10, pady = 10, column = 3, row = 1, columnspan = 5)
            
        find_root.mainloop()
        
        
    findbutton = CTkButton(master = root, width = 250, text = "Find", command = find)

    findbutton.grid (column = 3, row = 4, padx = 10, pady = 10)

    morebutton = CTkButton(master = root, width = 250, text = "More...", command = "")

    morebutton.grid (column = 4, row = 4)


    # tree view of all records #####################################
    style = ttk.Style()

    style.theme_use("clam")

    style.configure("Treeview", background = "darkgray", foreground = "black", rowheight = 30, fieldbackground = "darkgray")

    style.map("Treeview", background = [("selected", "green")])

    my_tree = ttk.Treeview(root)

    my_tree['columns'] = ("Name", "Lastname", "Age", "Fee", "Mobile")

    my_tree.column ("#0", width= 0, stretch = NO)

    my_tree.column ("Name", width= 270, anchor = CENTER)

    my_tree.column ("Lastname", width= 270, anchor = CENTER)

    my_tree.column ("Age", width= 270, anchor = CENTER)

    my_tree.column ("Fee", width= 270, anchor = CENTER)

    my_tree.column ("Mobile", width= 250, anchor = CENTER)

    ##### headings
    my_tree.heading("#0", text = "No", anchor = CENTER)

    my_tree.heading("Name", text = "Name", anchor = CENTER)

    my_tree.heading("Lastname", text = "Last Name", anchor = CENTER)

    my_tree.heading("Age", text = "Age", anchor = CENTER)

    my_tree.heading("Fee", text = "Fee", anchor = CENTER)

    my_tree.heading("Mobile", text = "Mobile", anchor = CENTER)

    records = cursor.execute("select  * from student")
    

    my_tree.tag_configure("oddrow", background="darkgray", foreground = "white")

    my_tree.tag_configure("evenrow", background = "gray", foreground = "white")

    iid1 = 0

    for record in records:
        
        if iid1 % 2 == 0:
            
            my_tree.insert( parent = "", index = "end", iid = iid1, values = (record[0], record[1], record[2], record[3], record[4]), tags = ("evenrow",))
        
        else:
            
            my_tree.insert( parent = "", index = "end", iid = iid1, values = (record[0], record[1], record[2], record[3], record[4]), tags = ("oddrow",))

            
        iid1 += 1
        
    my_tree.grid (column = 0, columnspan=5, pady = 20, padx = 10, row = 5, rowspan=13)

    updatebutton = CTkButton(master = root, width = 250, text = "Update", command = update)

    updatebutton.grid (column = 1, row = 4, padx = 10, pady = 10)
    
    countstudentslabel = CTkLabel(master = root, font=CTkFont(family = "roman", size = 20, weight = "bold"))
    
    countstudentslabel.grid(column = 0, row = 18, padx = 10, pady = 10, columnspan = 5)
    
    counter = 0
    
    countname = cursor.execute("select name from student")
    
    for countingname in countname:
        
        counter += 1
        
        countstudentslabel.configure(text = f"Total number of students: {counter}")
    

    root.mainloop()
    
    connection.close()
    
splash_root.after(5000, main_window)

splash_root.mainloop()