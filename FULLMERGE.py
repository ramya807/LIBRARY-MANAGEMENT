from tkinter import *

import pyttsx3

engine = pyttsx3.init()
def func_for_file1():
    from PIL import ImageTk, Image

    roota = Tk()

    roota.title("LIBRARY MANAGEMENT")  # Title of the application
    roota.geometry('500x500+400+100')  # Size of the screen
    image = Image.open(
        "C:\\Users\hp\Desktop\\image.jpg")
    # Resize the image using resize() method
    resize_image = image.resize((1000, 500))
    img = ImageTk.PhotoImage(resize_image)
    # create label and add resize image
    label1 = Label(image=img)
    label1.image = img
    label1.pack()
    Label(text='LIBRARY MANAGEMENT', fg='red', font=44).pack()  # text size and color of the topic


    Chooser = Menu()  # chooser is used for menubar
    itemone = Menu()  # itemone is display for the topics which comes under the my-profile
    itemone.add_command(label='LOGIN', command=func_for_file2)  # topic one under my-profile

    itemtwo = Menu()  # itemthree is display for the topics which comes under the hostels
    itemtwo.add_command(label='ISSUE BOOK', command=func_for_file3)
    itemtwo.add_command(label='RETURN BOOK', command=func_for_file4)

    itemthree = Menu()  # itemfour is display for the topics which comes under the warden
    itemthree.add_command(label='STAFF RECORD', command=func_for_file5)
    itemthree.add_command(label='STUDENT RECORD', command=func_for_file6)

    itemfour = Menu()  # itemfive is display for the topics which comes under the payment list
    itemfour.add_command(label='RULES AND REGULATIONS', command=func_for_file7)

    itemfive = Menu()  # itemfive is display for the topics which comes under the payment list
    itemfive.add_command(label='ADMIN USER', command=func_for_file8)
    itemfive.add_command(label='STUDENT USER', command=func_for_file9)

    # Used to view in screen all the labels in menubar
    Chooser.add_cascade(label='MY PROFILE', menu=itemone)
    Chooser.add_cascade(label='BOOK', menu=itemtwo)
    Chooser.add_cascade(label='RECORD', menu=itemthree)
    Chooser.add_cascade(label='RULES', menu=itemfour)
    Chooser.add_cascade(label='USERS', menu=itemfive)

    roota.config(menu=Chooser)
    roota.mainloop()

def func_for_file2():

    import tkinter.messagebox as tkMessageBox
    import sqlite3

    root = Tk()
    root.title("Login Page")

    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # =======================================VARIABLES=====================================
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()

    # =======================================METHODS=======================================
    def Database():
        global conn, cursor
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

    def LOGOUT():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    def LoginForm():
        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP, pady=80)
        lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = Button(LoginFrame, text="LOGIN", font=('arial', 18), width=35, command=Login)
        btn_login.grid(row=4, columnspan=2, pady=20)
        lbl_register = Label(LoginFrame, text="Register", fg="Dark Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', ToggleToRegister)

    def RegisterForm():
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40)
        lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result2.grid(row=5, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
        firstname.grid(row=3, column=1)
        lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
        lastname.grid(row=4, column=1)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
        btn_login.grid(row=6, columnspan=2, pady=20)
        lbl_login = Label(RegisterFrame, text="Login", fg="Dark Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)

    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()

    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()

    def Register():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
            lbl_result2.config(text="Please complete the required field!", fg="DARK RED")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)",
                               (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()

    def Login():
        Database()
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                lbl_result1.config(text="You Successfully Login", fg="blue")
            else:
                lbl_result1.config(text="Invalid Username or password", fg="red")

    LoginForm()

    # ========================================MENUBAR WIDGETS==================================
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="LOGOUT", command=LOGOUT)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # ========================================INITIALIZATION===================================
    if __name__ == '__main__':
        root.mainloop()

def func_for_file3():


    root = Tk()
    root.title("ISSUE BOOK")

    root.geometry('400x500')

    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=10)

    Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable=Name, width=50).pack()

    Label(frame1, text='Issue No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable=Number, width=50).pack()

    Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
    address = Text(frame2, width=37, height=10)
    address.pack()

    Button(root, text="Add", font="arial 12 bold").place(x=100, y=270)
    Button(root, text="View", font="arial 12 bold").place(x=100, y=310)
    Button(root, text="Delete", font="arial 12 bold").place(x=100, y=350)
    Button(root, text="Reset", font="arial 12 bold").place(x=100, y=390)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200, y=260)

    root.mainloop()


def func_for_file4():
    # Import Module


    # Create Object
    root = Tk()
    root.title("ISSUE BOOK")
    # Set geometry
    root.geometry('400x500')

    # Add Buttons, Label, ListBox
    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=10)

    Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable=Name, width=50).pack()

    Label(frame1, text='Issue No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable=Number, width=50).pack()

    Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
    address = Text(frame2, width=37, height=10)
    address.pack()

    Button(root, text="Add", font="arial 12 bold").place(x=100, y=270)
    Button(root, text="View", font="arial 12 bold").place(x=100, y=310)
    Button(root, text="Delete", font="arial 12 bold").place(x=100, y=350)
    Button(root, text="Reset", font="arial 12 bold").place(x=100, y=390)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config(command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200, y=260)

    root.mainloop()


def func_for_file5():
    # Importing the modules
    import tkinter
    import tkinter.ttk as ttk

    import sqlite3
    import tkinter.messagebox as tkMessageBox

    root = Tk()
    root.title("Staff Contact Management System")
    root.geometry("780x400+0+0")
    root.config(bg="light blue")

    # Variables required for storing the values
    f_name = StringVar()
    m_name = StringVar()
    l_name = StringVar()
    age = StringVar()
    home_address = StringVar()
    gender = StringVar()
    phone_number = StringVar()

    # Function for resetting the values
    def Reset():
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # For creating the database and the table
    def Database():
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `contactinformationn` (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT)")
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectnn.close()

    # Function for exiting the system
    def Exit():
        O = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
        if O > 0:
            root.destroy()
        return

    # Insert query for inserting the value in database Table
    def Submit():
        if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete All the Fields', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()

        cursor.execute(
            "INSERT INTO `contactinformationn` (first_name, middle_name, last_name, gender, age, home_address, phone_number ) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             int(phone_number.get())))

        connectnn.commit()
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()

        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connectnn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Update Query for updating the table in the database
    def Update():
        if gender.get() == "":
            msgg = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            tree.delete(*tree.get_children())
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute(
            "UPDATE `contactinformation` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?, `home_address` = ?, `phone_number` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()),
             str(home_address.get()),
             str(phone_number.get()), int(id)))
        connectnn.commit()
        cursor.execute("SELECT * FROM `contactinformationn` ORDER BY `last_name` ASC")
        fetchinfo = cursor.fetchall()
        for data in fetchinfo:
            tree.insert('', 'end', values=(data))
        gender1 = gender.get()
        if not gender1:
            tkMessageBox.showerror("Please select the gender")

        cursor.close()
        connectnn.close()

        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

    # Module for the update contact form window
    def UpdateContact(event):
        global id, UpdateWindow
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        id = item[0]
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        f_name.set(item[1])
        m_name.set(item[2])
        l_name.set(item[3])

        age.set(item[5])
        home_address.set(item[6])
        phone_number.set(item[7])

        UpdateWindow = Toplevel()
        UpdateWindow.title("Staff Contact Information")
        UpdateWindow.geometry("500x520+0+0")
        UpdateWindow.resizable(0, 0)
        if 'Opennewwindow' in globals():
            Opennewwindow.destroy()

        # FRAMES
        # module is for the frame, labels, text entry, and button for update contact form window
        FormTitle = Frame(UpdateWindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(UpdateWindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(
            side=LEFT)

        # LABELS
        label_title = Label(FormTitle, text="Update the Contact Informationn", font=('Arial', 17), bg="light green",
                            width=400)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text=" Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # TEXT ENTRY
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=2, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=2, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=2, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        #  Buttons
        ButtonUpdatContact = Button(ContactForm, text='Update', bd=2, font=('Calibri', 14, 'bold'), fg="black",
                                    bg="lightgreen", command=Update)
        ButtonUpdatContact.grid(row=8, columnspan=2, pady=10)

    # Delete query for deleting the value
    def Delete():
        if not tree.selection():
            msgg = tkMessageBox.showwarning('', 'Please Select the data!', icon="warning")
        else:
            msgg = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
        if msgg == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            item = contents['values']
            tree.delete(curItem)
        connectnn = sqlite3.connect("contactdataa.db")
        cursor = connectnn.cursor()
        cursor.execute("DELETE FROM `contactinformationn` WHERE `id` = %d" % item[0])
        connectnn.commit()
        cursor.close()
        connectnn.close()

    # For creating the frame, labels, text entry, and button for add new contact form window
    def MyNewContact():
        global opennewwindow
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")

        Opennewwindow = Toplevel()
        Opennewwindow.title("Staff Contact Details")
        Opennewwindow.resizable(0, 0)
        Opennewwindow.geometry("500x500+0+0")
        if 'UpdateWindow' in globals():
            UpdateWindow.destroy()

        #############Frames####################
        FormTitle = Frame(Opennewwindow)
        FormTitle.pack(side=TOP)
        ContactForm = Frame(Opennewwindow)
        ContactForm.pack(side=TOP, pady=10)
        RadioGroup = Frame(ContactForm)
        Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('Calibri', 14)).pack(side=LEFT)
        Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('Calibri', 14)).pack(
            side=LEFT)
        # ===================LABELS==============================
        label_title = Label(FormTitle, text="Adding New Contacts", bd=12, fg="black", bg="Lightgreen",
                            font=("Calibri", 15, "bold"), pady=2)
        label_title.pack(fill=X)
        label_FirstName = Label(ContactForm, text="First Name", font=('Calibri', 14), bd=5)
        label_FirstName.grid(row=0, sticky=W)

        label_MiddleName = Label(ContactForm, text="Middle Name", font=('Calibri', 14), bd=5)
        label_MiddleName.grid(row=1, sticky=W)

        label_LastName = Label(ContactForm, text="Last Name", font=('Calibri', 14), bd=5)
        label_LastName.grid(row=2, sticky=W)

        label_Gender = Label(ContactForm, text="Gender", font=('Calibri', 14), bd=5)
        label_Gender.grid(row=3, sticky=W)

        label_Age = Label(ContactForm, text="Age", font=('Calibri', 14), bd=5)
        label_Age.grid(row=4, sticky=W)

        label_HomeAddress = Label(ContactForm, text="Home Address", font=('Calibri', 14), bd=5)
        label_HomeAddress.grid(row=5, sticky=W)

        label_PhoneNumber = Label(ContactForm, text="Phone Number", font=('Calibri', 14), bd=5)
        label_PhoneNumber.grid(row=6, sticky=W)

        # ===================ENTRY===============================
        FirstName = Entry(ContactForm, textvariable=f_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                          justify='left')
        FirstName.grid(row=0, column=1)

        MiddleName = Entry(ContactForm, textvariable=m_name, font=('Calibri', 14, 'bold'), bd=3, width=20,
                           justify='left')
        MiddleName.grid(row=1, column=1)

        LastName = Entry(ContactForm, textvariable=l_name, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        LastName.grid(row=2, column=1)

        RadioGroup.grid(row=3, column=1)

        Age = Entry(ContactForm, textvariable=age, font=('Calibri', 14, 'bold'), bd=3, width=20, justify='left')
        Age.grid(row=4, column=1)

        HomeAddress = Entry(ContactForm, textvariable=home_address, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        HomeAddress.grid(row=5, column=1)

        PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('Calibri', 14, 'bold'), bd=3, width=20,
                            justify='left')
        PhoneNumber.grid(row=6, column=1)

        # ==================BUTTONS==============================
        ButtonAddContact = Button(ContactForm, text='Please Save', bd=5, font=('Calibri', 12, 'bold'), fg="black",
                                  bg="lightgreen", command=Submit)
        ButtonAddContact.grid(row=7, columnspan=2, pady=10)

    # module for whole frame window, labels and button of contact management system
    # ============================FRAMES======================================
    Top = Frame(root, width=600, bd=1)
    Top.pack(side=TOP)
    M = Frame(root, width=650, bg="light blue")
    M.pack(side=BOTTOM)
    F = Frame(width=7, height=8, bd=10, bg="light blue")
    F.pack(side=BOTTOM)
    MR = Frame(M, width=100)  # Right Middle frame
    MR.pack(side=RIGHT, pady=10)
    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    # LABELS
    label_title = Label(Top, text="Staff Contact System", bd=7, relief=GROOVE, fg="dark Blue", bg="lightgreen",
                        font=("Calibri", 25, "bold"), pady=3)
    label_title.pack(fill=X)

    # BUTTONS
    Add_Button = Button(F, text='Add New Contact', font=('Calibri', 17, 'bold'), fg="dark blue",
                        bg="lightgreen", command=MyNewContact).grid(row=0, column=0, ipadx=20, padx=30)

    Delete_Button = Button(F, text='Delete The Contact', font=('Calibri', 17, 'bold'), command=Delete,
                           fg="dark blue", bg="lightgreen").grid(row=0, column=1, ipadx=20)

    Exit_Button = Button(F, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
                         fg="dark blue", bg="lightgreen").grid(row=0, column=2, ipadx=20, padx=30)

    # creating a tables in contact management system
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(
    "Id", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Home Address", "Phone Number"),
                        height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Id', text="Id", anchor=W)
    tree.heading('First Name', text="First Name", anchor=W)
    tree.heading('Middle Name', text="Middle Name", anchor=W)
    tree.heading('Last Name', text="Last Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Home Address', text="Home Address", anchor=W)
    tree.heading('Phone Number', text="phone Number", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.column('#6', stretch=NO, minwidth=0, width=30)
    tree.column('#7', stretch=NO, minwidth=0, width=120)

    tree.pack()
    tree.bind('<Double-Button-1>', UpdateContact)

    # ============================INITIALIZATION==============================
    if __name__ == '__main__':
        Database()
    root.mainloop()


def func_for_file6():
    import datetime

    import tkinter.messagebox as mb
    from tkinter import ttk
    from typing import Any, Literal

    from tkcalendar import DateEntry  # pip install tkcalendar
    import sqlite3

    headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
    labelfont = ('Garamond', 14)
    entryfont = ('Garamond', 12)

    connector = sqlite3.connect('LibraryManagement.db')
    cursor = connector.cursor()
    connector.execute(
        "CREATE TABLE IF NOT EXISTS LIBRARY_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, "
        "EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT) "
    )

    def reset_fields():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
            exec(f"{i}.set('')")
        dob.set_date(datetime.datetime.now().date())

    def reset_form():
        global tree
        tree.delete(*tree.get_children())
        reset_fields()

    def display_records():
        tree.delete(*tree.get_children())
        curr = connector.execute('SELECT * FROM LIBRARY_MANAGEMENT')
        data = curr.fetchall()
        for records in data:
            tree.insert('', END, values=records)

    def add_record():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        name = name_strvar.get()
        email = email_strvar.get()
        contact = contact_strvar.get()
        gender = gender_strvar.get()
        DOB = dob.get_date()
        stream = stream_strvar.get()
        if not name or not email or not contact or not gender or not DOB or not stream:
            mb.showerror('Error!', "Please fill all the missing fields!!")
        else:
            try:
                connector.execute(
                    'INSERT INTO LIBRARY_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)',
                    (name, email, contact, gender, DOB, stream)
                )
                connector.commit()
                mb.showinfo('Record added', f"Record of {name} was successfully added")
                reset_fields()
                display_records()
            finally:
                mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact '
                                           'field can only ''contain numbers')

    def remove_record():
        if not tree.selection():
            mb.showerror('Error!', 'Please select an item from the database')
        else:
            current_item = tree.focus()
            values = tree.item(current_item)
            selection = values["values"]
            tree.delete(current_item)
            connector.execute('DELETE FROM LIBRARY_MANAGEMENT WHERE STUDENT_ID=%d')
            connector.commit()
            mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
            display_records()

    def view_record():
        global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
        if not tree.selection():
            mb.showerror('Error!', 'Please select a record to view')
        else:
            current_item = tree.focus()
            values = tree.item(current_item)
            selection: str | list[str] | Literal[""] | list[Any] | bool = values["values"]

            name_strvar.set(selection[1])
            email_strvar.set(selection[2])
            contact_strvar.set(selection[3])
            gender_strvar.set(selection[4])
            date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
            dob.set_date(date)
            stream_strvar.set(selection[6])

    main = Tk()
    main.title('DataFlair Library Management System')
    main.geometry('1250x600')
    # Creating the background and foreground color variables
    lf_bg = 'MediumSpringGreen'  # bg color for the left_frame
    cf_bg = 'Beige'  # bg color for the center_frame
    # Creating the StringVar or IntVar variables
    name_strvar = StringVar()
    email_strvar = StringVar()
    contact_strvar = StringVar()
    gender_strvar = StringVar()
    stream_strvar = StringVar()
    # Placing the components in the main window
    Label(main, text="LIBRARY MANAGEMENT SYSTEM", font=headlabelfont, bg='Blue').pack(side=TOP, fill=X)
    left_frame = Frame(main, bg=lf_bg)
    left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
    center_frame = Frame(main, bg=cf_bg)
    center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
    right_frame = Frame(main, bg="Gray35")
    right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)
    # Placing components in the left frame
    Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.05)
    Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
    Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
    Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.44)
    Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)
    Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.7)
    Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
    Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.23)
    Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.36)
    Entry(left_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=20, rely=0.75)
    OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.49, relwidth=0.5)
    dob = DateEntry(left_frame, font=("Arial", 12), width=15)
    dob.place(x=20, rely=0.62)
    Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.025,
                                                                                                         rely=0.85)
    # Placing components in the center frame
    Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.1,
                                                                                                      rely=0.25)
    Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.1, rely=0.35)
    Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.1, rely=0.45)
    Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.1,
                                                                                                     rely=0.55)
    # Placing components in the right frame
    Label(right_frame, text='Students Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP,
                                                                                                         fill=X)
    tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                        columns=(
                            'Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth",
                            "Stream"))
    X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
    X_scroller.pack(side=BOTTOM, fill=X)
    Y_scroller.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
    tree.heading('Student ID', text='ID', anchor=CENTER)
    tree.heading('Name', text='Name', anchor=CENTER)
    tree.heading('Email Address', text='Email ID', anchor=CENTER)
    tree.heading('Contact Number', text='Phone No', anchor=CENTER)
    tree.heading('Gender', text='Gender', anchor=CENTER)
    tree.heading('Date of Birth', text='DOB', anchor=CENTER)
    tree.heading('Stream', text='Stream', anchor=CENTER)
    tree.column('#0', width=0, stretch=NO)
    tree.column('#1', width=40, stretch=NO)
    tree.column('#2', width=140, stretch=NO)
    tree.column('#3', width=200, stretch=NO)
    tree.column('#4', width=80, stretch=NO)
    tree.column('#5', width=80, stretch=NO)
    tree.column('#6', width=80, stretch=NO)
    tree.column('#7', width=150, stretch=NO)
    tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
    display_records()

    # Finalizing the GUI window
    main.update()
    main.mainloop()


def func_for_file7():
    import tkinter as tk
    from tkinter.tix import Tk

    root = Tk()

    # specify size of window.
    root.geometry("550x310")

    # Create text widget and specify size.
    T = tk.Text(root, height=20, width=90)

    # Create label
    l = tk.Label(root, text="RULES AND REGULATION")
    l.config(font=("Courier", 14))

    Fact = """1)Library users must prominently display their Student ID on them at all times. Students 
    who fail to do so will not be allowed access to the Library facilities.

    2)No items belonging to the library are to be taken out of the library unless they have 
    been checked out at the Circulation Desk.

    3)Personal belongings should not be left unattended. The library management will not be
    held responsible for the loss of personal belongings.

    4)No food and drink (except plain water) are allowed in the library.

    5)Mobile phones or any other personal electronic gadgets must be switched to silent mode
    before entering the library.

    6)Making unreasonable noise, loud conversations, loud cell phone calls or playing loud 
    music or video that can distract other library users in the library is not permitted.

    7)Users are prohibited from making or answering calls within the quiet zone.

    8)Discussion room is used for academic purposes only and should not be used for private
    study or social purposes.

    9)Eating, drinking, sleeping and smoking are not allowed in the library.

    10)The Library users should be professionally attired, as specified in the student
    handbook. We reserve the right to deny entry to students who are inappropriately attired.

    11)Library furniture/equipment should not be moved from its original location.

    12)Personal Computers provided are to be strictly used for academic research and Library
    CD viewing only. These computers cannot be used for personal e-mail, online chatting or playing games.

    13)Library staffs reserve the right to inspect bags or other personal property when users
    enter or leave the library.

    14)When a user is caught for breaching the library rules and regulations, immediate 
    action will be taken."""

    # Create an Exit button.
    b2 = tk.Button(root, text="Exit",
                   command=root.destroy)

    l.pack()
    T.pack()
    b2.pack()

    # Insert The Fact.
    T.insert(tk.END, Fact)

    tk.mainloop()

def func_for_file8():

    import backend

    class admin:
        def __init__(self, window):
            self.window = window

            self.frame = Frame(self.window, bg='orange', width=800, height=450)

            self.frame.pack()

            self.label = Label(self.frame, text='Admin User', bg='Orange', font=('Georgia', 30, 'bold'))
            self.label.place(x=20, y=20, width=400, height=50)

            self.label_title = Label(self.frame, text='TITLE', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_title.place(x=20, y=100, width=100, height=50)

            self.label_year = Label(self.frame, text='YEAR', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_year.place(x=20, y=150, width=100, height=30)

            self.label_author = Label(self.frame, text='AUTHOR', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_author.place(x=350, y=100, width=100, height=30)

            self.label_isbn = Label(self.frame, text='ISBN', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_isbn.place(x=350, y=150, width=100, height=30)

            self.title_text = StringVar()
            self.entry_title = Entry(self.frame, fg='gray', textvariable=self.title_text, width=25,
                                     font=('Arial', 12, 'bold'))
            self.entry_title.place(x=120, y=100, width=150, height=30)

            self.year_text = StringVar()
            self.entry_year = Entry(self.frame, fg='gray', textvariable=self.year_text, width=25,
                                    font=('Arial', 12, 'bold'))
            self.entry_year.place(x=120, y=150, width=150, height=30)

            self.author_text = StringVar()
            self.entry_author = Entry(self.frame, fg='gray', textvariable=self.author_text, width=25,
                                      font=('Arial', 12, 'bold'))
            self.entry_author.place(x=470, y=100, width=150, height=30)

            self.isbn_text = StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray', textvariable=self.isbn_text, width=25,
                                    font=('Arial', 12, 'bold'))
            self.entry_isbn.place(x=470, y=150, width=150, height=30)

            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100, y=200, width=500, height=100)

            self.button_view = Button(self.frame, text='View All', command=self.view_command)
            self.button_view.place(x=100, y=320, width=100, height=40)

            self.button_search = Button(self.frame, text='Search ', command=self.search_command)
            self.button_search.place(x=200, y=320, width=100, height=40)

            self.button_add = Button(self.frame, text='Add entry', command=self.add_command)
            self.button_add.place(x=300, y=320, width=100, height=40)

            self.button_update = Button(self.frame, text='Update entry', command=self.update_command)
            self.button_update.place(x=400, y=320, width=100, height=40)

            self.button_delete = Button(self.frame, text='Delete entry', command=self.delete_command)
            self.button_delete.place(x=500, y=320, width=100, height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=100, y=360, width=100, height=40)

            self.button_request = Button(self.frame, text='Requested Books', command=self.requestsearch_command)
            self.button_request.place(x=300, y=360, width=100, height=40)

            self.button_issue = Button(self.frame, text='Issued Books', command=self.issuesearch_command)
            self.button_issue.place(x=500, y=360, width=100, height=40)

        def destroy(self):
            self.button_issuedelete.destroy()
            self.button_requestdelete.destroy()

        def clear_command(self):
            self.entry_title.delete(0, END)
            self.entry_year.delete(0, END)
            self.entry_author.delete(0, END)
            self.entry_isbn.delete(0, END)

        def issuedelete_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.issue_delete(value[0])
            self.entry_title.delete(0, END)
            # self.entry_title.insert(END,value[1])
            self.entry_year.delete(0, END)
            # self.entry_year.insert(END,value[3])
            self.entry_author.delete(0, END)
            # self.entry_author.insert(END,value[2])
            self.entry_isbn.delete(0, END)
            # self.entry_isbn.insert(END,value[4])

        def issuesearch_command(self):
            self.listbox.delete(0, END)  # it will empty the list every time it is called
            for row in backend.issue_view(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                          self.isbn_text.get()):
                self.listbox.insert(END, row)

            self.button_issuedelete = Button(self.frame, text='Book Returned', command=self.issuedelete_command)
            self.button_issuedelete.place(x=400, y=360, width=100, height=40)

        def requestsearch_command(self):
            self.listbox.delete(0, END)
            for row in backend.request_view(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                            self.isbn_text.get()):
                self.listbox.insert(END, row)

            self.button_requestdelete = Button(self.frame, text='Request Listened',
                                               command=self.requestcomplete_command)
            self.button_requestdelete.place(x=200, y=360, width=100, height=40)

        def requestcomplete_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.request_delete(value[0])
            self.entry_title.delete(0, END)
            # self.entry_title.insert(END,value[0])
            self.entry_year.delete(0, END)
            # self.entry_year.insert(END,value[2])
            self.entry_author.delete(0, END)
            # self.entry_author.insert(END,value[1])
            self.entry_isbn.delete(0, END)
            # self.entry_isbn.insert(END,value[3])

        def view_command(self):
            self.listbox.delete(0, END)
            for row in backend.view():
                self.listbox.insert(END, row)  # END ensures that every new entry is stored at end of the all rows
            self.destroy()

        def search_command(self):
            self.listbox.delete(0, END)
            for row in backend.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                      self.isbn_text.get()):
                self.listbox.insert(END, row)
                self.destroy()

        def add_command(self):
            backend.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
            self.listbox.delete(0, END)
            self.listbox.insert(END, (
            self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))
            self.destroy()

        def delete_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            backend.delete(value[0])  # i have to use value[0] here or at backend use id[0]
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, value[1])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, value[3])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, value[2])
            self.entry_isbn.delete(0, END)
            self.entry_isbn.insert(END, value[4])
            self.destroy()

        def update_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, value[0])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, value[2])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, value[1])
            self.entry_isbn.delete(0, END)
            self.entry_isbn.insert(END, value[3])
            backend.update(value[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                           self.isbn_text.get())

    window = Tk()
    window.title('Admin_User')
    window.geometry('700x450')
    obj = admin(window)
    window.mainloop()

def func_for_file9():

    from tkinter import ttk, messagebox
    import backend

    class student:
        def __init__(self, window):
            self.window = window

            self.frame = Frame(self.window, bg='orange', width=700, height=400)

            self.label = Label(self.frame, text='Student User', bg='Orange', font=('Georgia', 30, 'bold'))
            self.label.place(x=20, y=20, width=400, height=50)

            self.label_title = Label(self.frame, text='TITLE', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_title.place(x=20, y=100, width=100, height=50)

            self.label_year = Label(self.frame, text='YEAR', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_year.place(x=20, y=150, width=100, height=30)

            self.label_author = Label(self.frame, text='AUTHOR', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_author.place(x=350, y=100, width=100, height=30)

            self.label_isbn = Label(self.frame, text='ISBN', bg='orange', font=('Georgia', 14, 'bold'))
            self.label_isbn.place(x=350, y=150, width=100, height=30)

            self.title_text = StringVar()
            self.entry_title = Entry(self.frame, fg='gray', textvariable=self.title_text, width=25,
                                     font=('Arial', 12, 'bold'))
            self.entry_title.place(x=120, y=100, width=150, height=30)

            self.year_text = StringVar()
            self.entry_year = Entry(self.frame, fg='gray', textvariable=self.year_text, width=25,
                                    font=('Arial', 12, 'bold'))
            self.entry_year.place(x=120, y=150, width=150, height=30)

            self.author_text = StringVar()
            self.entry_author = Entry(self.frame, fg='gray', textvariable=self.author_text, width=25,
                                      font=('Arial', 12, 'bold'))
            self.entry_author.place(x=470, y=100, width=150, height=30)

            self.isbn_text = StringVar()
            self.entry_isbn = Entry(self.frame, fg='gray', textvariable=self.isbn_text, width=25,
                                    font=('Arial', 12, 'bold'))
            self.entry_isbn.place(x=470, y=150, width=150, height=30)

            self.listbox = Listbox(self.frame)
            self.listbox.place(x=100, y=200, width=500, height=100)

            self.button_view = Button(self.frame, text='View All', command=self.view_command)
            self.button_view.place(x=100, y=320, width=100, height=40)

            self.button_search = Button(self.frame, text='Search ', command=self.search_command)
            self.button_search.place(x=200, y=320, width=100, height=40)

            self.button_issue = Button(self.frame, text='Issue', command=self.issue_command)
            self.button_issue.place(x=300, y=320, width=100, height=40)

            self.button_request = Button(self.frame, text='Request', command=self.request_command)
            self.button_request.place(x=400, y=320, width=100, height=40)

            self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
            self.button_issue.place(x=500, y=320, width=100, height=40)

            self.frame.pack()

        def clear_command(self):
            self.entry_title.delete(0, END)
            self.entry_year.delete(0, END)
            self.entry_author.delete(0, END)
            self.entry_isbn.delete(0, END)

        def request_command(self):
            backend.request_insert(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                   self.isbn_text.get())
            self.listbox.delete(0, END)
            self.listbox.insert(END, (
            self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

        def issue_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, value[1])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, value[2])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, value[3])
            self.entry_isbn.delete(0, END)
            self.entry_isbn.insert(END, value[4])
            backend.issue_insert(value[0])

        def view_command(self):
            self.listbox.delete(0, END)
            for row in backend.view():
                self.listbox.insert(END, row)

        def search_command(self):
            self.listbox.delete(0, END)
            for row in backend.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                      self.isbn_text.get()):
                self.listbox.insert(END, row)

        def add_command(self):
            backend.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
            self.listbox.delete(0, END)
            self.listbox.insert(END, (
            self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

        def delete_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, value[1])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, value[2])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, value[3])
            self.entry_isbn.delete(0, END)
            self.entry_isbn.insert(END, value[4])
            backend.delete(value[0])

        def update_command(self):
            selected_tuple = self.listbox.curselection()
            value = self.listbox.get(selected_tuple)
            self.entry_title.delete(0, END)
            self.entry_title.insert(END, value[0])
            self.entry_year.delete(0, END)
            self.entry_year.insert(END, value[1])
            self.entry_author.delete(0, END)
            self.entry_author.insert(END, value[2])
            self.entry_isbn.adelete(0, END)
            self.entry_isbn.insert(END, value[3])
            backend.update(value[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                           self.isbn_text.get())

    window = Tk()
    window.title('Student_User')
    window.geometry('700x400')
    obj = student(window)
    window.mainloop()

    # ============================INITIALIZATION==============================
    if __name__ == '_main_':
        Database()
    root.mainloop()


def main():
    # Decide what order you want to call these methods.
    func_for_file1()


if __name__ == '__main__':
    main()